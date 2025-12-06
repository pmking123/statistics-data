# birthwt.csv Codebook

**Filename:** `birthwt.csv`  
**Source:** Partially taken from Rebecca Nugent, Department of Statistics, University of Washington  
**Purpose in course:** Useful as an example dataset for logistic regression.

---

## Variables

Fill in one row per column in `birthwt.csv`.

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `low`   | factor: 0 = not low birthweight, 1 = low birthweight   |       | Whether baby had low birthweight  |
| `age`   | numeric                  | years | Mother's age|
| `lwt`   | numeric                  | lbs   | Mother's weight in pounds|
| `race`  | factor: 1 = white, 2 = black, 3 = other       |       | Mother's race |
| `smoke` | factor: 0 = non-smoker, 1 = smoker        |       | Smoking status during pregnancy |
| `ptd`   | numeric        |       | Number of previous premature labors |
| `ht`    | factor: 0 = no hypertension, 1 = hypertension        |       | History of hypertension |
| `ui`    | factor: 0 = no uterine irritability, 1 = uterine irritability        |       | Presence of uterine irritability |
| `ftv`   | numeric |       | Number of physician visits during the first trimester of pregnancy|
| `bwt`   | numeric | grams | Birth weight of the baby in grams|

---

## Notes

None

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/birthwt.csv", header = TRUE)
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/birthwt.csv")
```
