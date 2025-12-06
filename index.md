# Statistics data — dataset index

Welcome! This site provides access to datasets used in statistics modules.

- All **stand‑alone datasets** live in the `datasets/` folder.
- Textbook‑specific datasets live in `textbook_data/` (each subfolder has its own README).

You can browse everything via GitHub Pages at:

```text
https://pmking123.github.io/statistics-data/
```

or directly on GitHub at:

```text
https://github.com/pmking123/statistics-data
```

---

## 1. Core datasets (from `datasets/`)

Each dataset has:

- a CSV file you can load into R, Python, or Excel;
- a matching Markdown codebook (`.md`) that explains its variables.

The links below use **relative paths**, so they work on both:

- GitHub Pages (as web URLs), and
- the GitHub repository (as file links).

| Dataset | CSV | Codebook |
|---------|-----|----------|
| Anscombe's quartet — set 1 | [`Anscombe_1.csv`](datasets/Anscombe_1.csv) | [`Anscombe_1.md`](datasets/Anscombe_1.md) |
| Anscombe's quartet — set 2 | [`Anscombe_2.csv`](datasets/Anscombe_2.csv) | [`Anscombe_2.md`](datasets/Anscombe_2.md) |
| Anscombe's quartet — set 3 | [`Anscombe_3.csv`](datasets/Anscombe_3.csv) | [`Anscombe_3.md`](datasets/Anscombe_3.md) |
| Anscombe's quartet — set 4 | [`Anscombe_4.csv`](datasets/Anscombe_4.csv) | [`Anscombe_4.md`](datasets/Anscombe_4.md) |
| Biochemical oxygen demand | [`BOD.csv`](datasets/BOD.csv) | [`BOD.md`](datasets/BOD.md) |
| Plant CO₂ uptake | [`CO2.csv`](datasets/CO2.csv) | [`CO2.md`](datasets/CO2.md) |
| Chick growth (longitudinal) | [`ChickWeight.csv`](datasets/ChickWeight.csv) | [`ChickWeight.md`](datasets/ChickWeight.md) |
| Iris data (3‑species classification) | [`iris.csv`](datasets/iris.csv) | [`iris.md`](datasets/iris.md) |
| Body dimensions (anthropometry) | [`bdims.csv`](datasets/bdims.csv) | [`bdims.md`](datasets/bims.md) |
| Heights and weights of women | [`women.csv`](datasets/women.csv) | [`women.md`](datasets/women.md) |

> **Note:** This table only lists some of the most commonly used datasets.  
> You can extend it by adding more rows following the same pattern.

---

## 2. Textbook datasets (`textbook_data/`)

Datasets that come from specific textbooks are organised into subfolders:

| Folder | Description |
|--------|-------------|
| [`textbook_data/Barton_Peat`](textbook_data/Barton_Peat) | Datasets from Barton & Peat |
| [`textbook_data/Glantz-Slinker`](textbook_data/Glantz-Slinker) | Datasets from Glantz & Slinker |
| [`textbook_data/OpenIntro`](textbook_data/OpenIntro) | Datasets from *OpenIntro Statistics* |
| [`textbook_data/Samuels_Witmer`](textbook_data/Samuels_Witmer) | Datasets from Samuels & Witmer |
| [`textbook_data/Samuels_Witmer_4e`](textbook_data/Samuels_Witmer_4e) | Additional datasets from the 4th edition |

Each of these folders contains its own `README.md` describing the datasets inside it.  
Consult those READMEs plus any per‑dataset codebooks when working with textbook data.

---

## 3. How to load these datasets

See the separate page: [`using-data.md`](using-data.md) for detailed instructions on:

- loading datasets directly from the web in **R** and **Python**;
- downloading datasets for use in **Excel**;
- good practice for citing dataset sources in your scripts.

---

## 4. Conventions

- CSV files contain **data only** (no comments or metadata rows).
- Variable names, units and explanations live in the corresponding `*.md` codebooks.
- Folder‑level `README.md` files summarise the contents of each collection.
