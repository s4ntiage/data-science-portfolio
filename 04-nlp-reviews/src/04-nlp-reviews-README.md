# 04 — Product Review Analyzer · Amazon

> **NLP · Sentiment Analysis · Topic Modeling**

NLP pipeline to extract insights from Amazon product reviews at scale. Compares classical sentiment analysis (VADER) with a fine-tuned transformer (DistilBERT), and uses BERTopic for unsupervised topic discovery — all without manual labeling.

---

## Highlights

- **VADER vs. BERT** sentiment comparison with F1 scores and disagreement analysis
- **BERTopic** topic modeling — discovers themes like "battery life" or "packaging quality" automatically
- **Named Entity Recognition** to extract brand/product mentions
- Sentiment trend over time, broken down by product category
- A proper **model card** documenting limitations — shows clients you think about responsible ML, not just metrics

## Key Finding

> BERT outperforms VADER by **~14 F1 points**, with the largest gains on sarcastic and mixed-sentiment reviews where rule-based sentiment fails.

---

## Structure

```
04-nlp-reviews/
├── notebooks/
│   └── nlp_review_analyzer.ipynb   ← main pipeline
├── src/                              ← (optional) reusable scripts
└── README.md
```

## Setup

```bash
pip install transformers torch bertopic nltk scikit-learn pandas datasets matplotlib seaborn
```

**Data:** Loaded automatically from the [Amazon Polarity dataset](https://huggingface.co/datasets/amazon_polarity) via Hugging Face `datasets`. No manual download needed.

**Note:** Running the BERT and NER pipelines on CPU works but is slow on the full sample — the notebook uses manageable subsets (1,000–2,000 reviews) for demo speed. For production-scale runs, use a GPU.

## Tools

![Transformers](https://img.shields.io/badge/-🤗%20Transformers-FFD21E?style=flat)
![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![BERTopic](https://img.shields.io/badge/-BERTopic-1A1A2E?style=flat)
![NLTK](https://img.shields.io/badge/-NLTK-154F3C?style=flat)

---

*Dataset: Amazon Polarity (Hugging Face) · For educational/portfolio purposes*
