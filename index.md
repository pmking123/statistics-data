# 📘 Statistics Dataset Library

Welcome!  
This site provides easy access to datasets used across statistics modules.

Use the links below to browse, download, or load datasets directly into **R**, **Python**, or **Excel**.

👉 For help using the data, see:  
**[How to load datasets](using-data.md)**

---

# 🔍 1. Core datasets (`datasets/`)

These datasets are stored as clean CSVs and include a matching codebook.

| Dataset | CSV | Codebook |
|---------|-----|----------|
| Anscombe’s quartet (set 1) | [`Anscombe_1.csv`](datasets/Anscombe_1.csv) | [`Anscombe_1.md`](datasets/Anscombe_1.md) |
| Anscombe’s quartet (set 2) | [`Anscombe_2.csv`](datasets/Anscombe_2.csv) | [`Anscombe_2.md`](datasets/Anscombe_2.md) |
| Anscombe’s quartet (set 3) | [`Anscombe_3.csv`](datasets/Anscombe_3.csv) | [`Anscombe_3.md`](datasets/Anscombe_3.md) |
| Anscombe’s quartet (set 4) | [`Anscombe_4.csv`](datasets/Anscombe_4.csv) | [`Anscombe_4.md`](datasets/Anscombe_4.md) |
| Biochemical oxygen demand | [`BOD.csv`](datasets/BOD.csv) | [`BOD.md`](datasets/BOD.md) |
| Iris flower dataset | [`iris.csv`](datasets/iris.csv) | [`iris.md`](datasets/iris.md) |
| Chick growth | [`ChickWeight.csv`](datasets/ChickWeight.csv) | [`ChickWeight.md`](datasets/ChickWeight.md) |
| Body dimensions | [`bdims.csv`](datasets/bdims.csv) | [`bdims.md`](datasets/bdims.md) |
| Women’s heights/weights | [`women.csv`](datasets/women.csv) | [`women.md`](datasets/women.md) |

Browse the full folder here:  
👉 [`datasets/`](datasets/)

---

# 📚 2. Textbook datasets (`textbook_data/`)

| Folder | Description |
|--------|-------------|
| [`textbook_data/Barton_Peat`](textbook_data/Barton_Peat) | Barton & Peat datasets |
| [`textbook_data/Glantz-Slinker`](textbook_data/Glantz-Slinker) | Glantz & Slinker |
| [`textbook_data/OpenIntro`](textbook_data/OpenIntro) | *OpenIntro Statistics* |
| [`textbook_data/Samuels_Witmer`](textbook_data/Samuels_Witmer) | Samuels & Witmer |
| [`textbook_data/Samuels_Witmer_4e`](textbook_data/Samuels_Witmer_4e) | 4th edition datasets |

---

# 🧭 3. Loading datasets into R / Python

Example using **BOD.csv**:

### R
```r
url <- "https://pmking123.github.io/statistics-data/datasets/BOD.csv"
dat <- read.csv(url)
```

or

```r
library(readr)
url <- "https://pmking123.github.io/statistics-data/datasets/BOD.csv"
dat <- read_csv(url)
```

### Python
```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/BOD.csv")
```

See full guidance here:  
👉 **[using-data.md](using-data.md)**

---

# 📄 Notes

- CSV files contain *raw data only*.  
- Variable descriptions appear in the dataset’s codebook (`*.md`).  
- GitHub Pages updates after each push.

---

# 🎓 Happy analysing!
