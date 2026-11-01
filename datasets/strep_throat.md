# strep_throat.csv Codebook

- **Filename:** `strep_throat.csv`  
- **Source:** simulated data
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/strep_throat.csv](https://pmking123.github.io/statistics-data/datasets/strep_throat.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `id`              | numeric | | Child identifier |
| `age`             | numeric | years | Age of the child (3–14) |
| `culture`         | factor: Positive / Negative | | Throat culture for group A *Streptococcus* (reference standard) |
| `rapid_antigen`   | factor: Positive / Negative | | Rapid antigen detection test, read in the surgery |
| `rapid_molecular` | factor: Positive / Negative | | Rapid molecular (nucleic acid amplification) test |

---

## Notes

A simulated diagnostic-accuracy study of 400 children who visited their GP with a sore throat. Each child had a throat swab tested three ways, so the two rapid tests are **paired** (the same children had both). 120 children (30%) were culture-positive.

The cell counts were set directly so that the rapid antigen test has sensitivity 0.85 and specificity 0.957, and the molecular test sensitivity 0.95 and specificity 0.964. The performance figures are illustrative, not taken from a particular study. `age` is random and unrelated to the other variables.

Used in Workshop 6 (diagnostic accuracy; McNemar's test for paired proportions).

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/strep_throat.csv", header = TRUE)
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/strep_throat.csv")
```
