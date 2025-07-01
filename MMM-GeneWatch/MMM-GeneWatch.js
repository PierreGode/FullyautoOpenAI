Module.register("MMM-GeneWatch", {
  defaults: {
    updateInterval: 6 * 60 * 60 * 1000,
    showTags: true,
    maxItems: 3,
    sources: ["bioRxiv", "Nature", "Science"],
    useGPTSummary: true,
    openaiApiKey: ""
  },

  start: function() {
    this.items = [];
    this.scheduleUpdate();
    this.sendSocketNotification("GENEWATCH_UPDATE", this.config);
  },

  scheduleUpdate: function() {
    clearTimeout(this.updateTimer);
    this.updateTimer = setTimeout(() => {
      this.sendSocketNotification("GENEWATCH_UPDATE", this.config);
    }, this.config.updateInterval);
  },

  getStyles: function() {
    return ["styles.css"];
  },

  socketNotificationReceived: function(notification, payload) {
    if (notification === "GENEWATCH_DATA") {
      this.items = payload;
      this.updateDom();
      this.scheduleUpdate();
    }
  },

  getDom: function() {
    const wrapper = document.createElement("div");
    if (!this.items || this.items.length === 0) {
      wrapper.innerHTML = "No biotech news available.";
      return wrapper;
    }
    this.items.forEach(item => {
      const itemContainer = document.createElement("div");
      itemContainer.className = "genewatch-item";

      const title = document.createElement("a");
      title.href = item.link;
      title.target = "_blank";
      title.textContent = item.title;
      title.className = "genewatch-title";
      itemContainer.appendChild(title);

      if (item.summary) {
        const summary = document.createElement("div");
        summary.textContent = item.summary;
        summary.className = "genewatch-summary";
        itemContainer.appendChild(summary);
      }

      if (this.config.showTags && item.tags && item.tags.length) {
        const tags = document.createElement("div");
        tags.className = "genewatch-tags";
        item.tags.forEach(tag => {
          const tagElem = document.createElement("span");
          tagElem.className = "genewatch-tag";
          tagElem.textContent = tag;
          tags.appendChild(tagElem);
        });
        itemContainer.appendChild(tags);
      }

      wrapper.appendChild(itemContainer);
    });
    return wrapper;
  }
});