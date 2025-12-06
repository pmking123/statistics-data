# statistics-data

This repository hosts datasets used across statistics teaching modules.  
It provides:

- Clean CSV data files (no embedded comments or metadata)  
- Matching Markdown **codebooks** documenting each dataset  
- Textbook-specific datasets organised into subfolders  
- A student-friendly GitHub Pages site for easy access:

👉 **https://pmking123.github.io/statistics-data/**

---

## 📚 Repository structure

```
statistics-data/
│
├── README.md                 ← This file (for GitHub users)
├── index.md                  ← Student landing page (GitHub Pages)
├── using-data.md             ← How students load datasets
│
├── datasets/                 ← Stand-alone datasets + codebooks
│     ├── BOD.csv
│     ├── BOD.md
│     ├── iris.csv
│     ├── iris.md
│     └── …
│
└── textbook_data/            ← Data grouped by textbook
      ├── Barton_Peat/
      ├── Glantz-Slinker/
      ├── OpenIntro/
      ├── Samuels_Witmer/
      └── Samuels_Witmer_4e/
```

All datasets in `datasets/` are directly accessible via short URLs such as:

```
https://pmking123.github.io/statistics-data/datasets/BOD.csv
```

---

## 📄 Codebooks

Each dataset has a corresponding `*.md` codebook containing:

- Variable definitions  
- Units  
- Notes on missing values or structure  
- Example loading code (R and Python)

---

## 🔗 GitHub Pages (student site)

The student-facing documentation and dataset browser is available at:

👉 **https://pmking123.github.io/statistics-data/**  

---

## 👨‍🏫 Maintaining the repository

1. Add or update files in `datasets/` or `textbook_data/`.
2. Update or add codebooks.
3. Update dataset lists in `index.md` (or use `tools/make_dataset_table.py`).
4. Commit + push.
5. GitHub Pages updates automatically.

---

## 🧰 Tools included

Inside `tools/`:

- **make_dataset_table.py** — auto-generates Markdown tables listing datasets and codebooks.

---

## 📄 License

These datasets are provided for educational purposes only.
