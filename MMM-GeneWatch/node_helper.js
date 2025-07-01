const NodeHelper = require("node_helper");
const Parser = require("rss-parser");
const OpenAI = require("openai");

const FEED_URLS = {
  bioRxiv: "https://www.biorxiv.org/rss/latest/genetics.xml",
  Nature: "https://www.nature.com/nbt.rss",
  Science: "https://www.science.org/rss/genetics.xml"
};

module.exports = NodeHelper.create({
  start: function() {
    this.parser = new Parser();
  },

  socketNotificationReceived: async function(notification, payload) {
    if (notification === "GENEWATCH_UPDATE") {
      this.config = payload;
      if (this.config.useGPTSummary && this.config.openaiApiKey) {
        this.openai = this.openai || new OpenAI({ apiKey: this.config.openaiApiKey });
      }
      this.fetchNews();
    }
  },

  fetchNews: async function() {
    const allItems = [];
    for (const source of this.config.sources) {
      const url = FEED_URLS[source] || source;
      try {
        const feed = await this.parser.parseURL(url);
        feed.items.slice(0, this.config.maxItems).forEach(item => {
          allItems.push({
            title: item.title,
            link: item.link,
            summary: "",
            tags: []
          });
        });
      } catch (e) {
        console.error(this.name, "Error fetching feed", source, e);
      }
    }
    for (const item of allItems) {
      const text = item.title + (item.summary || "");
      item.tags = ["CRISPR", "synthetic DNA", "mRNA", "AI drug design"].filter(keyword =>
        text.includes(keyword)
      );
      if (this.config.useGPTSummary && this.openai) {
        try {
          const response = await this.openai.chat.completions.create({
            model: "gpt-3.5-turbo",
            messages: [
              { role: "system", content: "You summarize biotechnology news." },
              { role: "user", content: `Summarize this in two sentences:\n${item.title}` }
            ]
          });
          item.summary = response.choices[0].message.content.trim();
        } catch (err) {
          console.error(this.name, "Error with GPT summarization", err);
        }
      }
    }
    this.sendSocketNotification("GENEWATCH_DATA", allItems.slice(0, this.config.maxItems));
  }
});