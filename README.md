
# statistics-data

This repository contains datasets used across statistics modules.  
All datasets are provided as **clean CSV files** with no embedded metadata.  
Each dataset has a matching **Markdown codebook** describing variables, units, and notes.

---

## 📄 Dataset Index

Below is a list of datasets in this repository.  
Each file links to its corresponding codebook (once created).

> **Note:** Codebook files will be named the same as the dataset, but with `.md` instead of `.csv`.  
> Example: `BOD.csv` → `BOD.md`.

| Dataset | Description | Codebook |
|---------|-------------|----------|
| `Anscombe_1.csv` | Anscombe's quartet — set 1 | `Anscombe_1.md` |
| `Anscombe_2.csv` | Anscombe's quartet — set 2 | `Anscombe_2.md` |
| `Anscombe_3.csv` | Anscombe's quartet — set 3 | `Anscombe_3.md` |
| `Anscombe_4.csv` | Anscombe's quartet — set 4 | `Anscombe_4.md` |
| `BOD.csv` | Biochemical oxygen demand over time | `BOD.md` |
| `CO2.csv` | CO₂ uptake in plants under varying conditions | `CO2.md` |
| *(add more rows as codebooks are created)* | | |

---

## 📥 Loading Data

### **R**
```r
df <- read.csv("filename.csv")
```

### **Python (pandas)**
```python
import pandas as pd
df = pd.read_csv("filename.csv")
```

### **Excel**
On GitHub, click a file → **Download raw**.

---

## 🧭 Repository Conventions

- CSV files contain **raw data only**, with no comments or metadata.
- Each dataset has a `.md` **codebook** stored in the same directory.
- If datasets live inside subfolders, each folder includes a `README.md` describing its contents.

---

## 📘 For Students

1. Find the dataset you are using (e.g., `CO2.csv`).  
2. Read the matching codebook (e.g., `CO2.md`).  
3. Load the CSV into R/Python/Excel.  
4. Refer back to the codebook whenever you need variable meanings or units.

---

## 📄 License

These datasets are provided for educational use in statistics courses.
