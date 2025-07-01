# 🧬 MMM-GeneWatch – Daily Biotech Breakthroughs

## 📋 Summary

`MMM-GeneWatch` is a MagicMirror² module that displays daily or real-time breakthroughs in biotechnology and genetic research. It is intended to keep users up-to-date with the latest developments in CRISPR, synthetic DNA, AI-designed medicines, and genomic science. Information is aggregated from reputable scientific journals and optionally summarized by GPT.

---

## 📡 Data Sources

- [Nature Biotechnology](https://www.nature.com/nbt/)
- [Science Magazine - Genetics Section](https://www.science.org/)
- [bioRxiv Preprints – Genetics/Bioinformatics](https://www.biorxiv.org/)
- Optional: GPT-generated summaries of articles using OpenAI API

---

## ⚙️ Features

- 🧠 Summarizes top 1–3 daily biotech news items
- 🧬 Tags discoveries: `CRISPR`, `synthetic DNA`, `mRNA`, `AI drug design`, etc.
- ⏳ Configurable refresh interval (e.g. every 6h or once daily)
- 📜 Minimalist mirror-friendly UI
- 🔗 Option to display original source link

---

## 🧰 Config Options (example)

```js
{
  module: "MMM-GeneWatch",
  position: "top_left",
  config: {
    updateInterval: 6 * 60 * 60 * 1000, // every 6 hours
    showTags: true,
    showSourceLink: true, // display original source link
    maxItems: 3,
    sources: ["bioRxiv", "Nature", "Science"],
    useGPTSummary: true,
    openaiApiKey: "YOUR_API_KEY"
  }
}

MMM-GeneWatch/
├── MMM-GeneWatch.js         # Frontend module display
├── node_helper.js           # Fetches and parses RSS feeds / GPT
├── styles.css               # Clean biotech-themed design
├── AGENT.md                 # This file

Goal
To inspire curiosity and awareness of cutting-edge bioscience—right from your mirror.