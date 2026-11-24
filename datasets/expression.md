# expression.csv Codebook

- **Filename:** `expression.csv`  
- **Source:** simulated data
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/expression.csv](https://pmking123.github.io/statistics-data/datasets/expression.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `sample`    | character | | Sample identifier (S01–S16) |
| `condition` | factor: control / treated | | Experimental condition |
| `batch`     | factor: day1 / day2 | | Day on which the sample was processed |
| `gene_01` … `gene_40` | numeric | log2 expression | Expression of 40 genes |

---

## Notes

A simulated gene-expression experiment: 16 samples (8 control, 8 treated), each measured for 40 genes. Each processing day handled 4 control and 4 treated samples, so batch and treatment are balanced (not confounded).

The data were generated with a known structure, so students can check what PCA and clustering recover:

- genes 1–10 are higher in treated samples (by 1.5 log2 units);
- genes 11–18 are lower in treated samples (by 1.2 log2 units);
- genes 19–24 are higher in samples processed on day 2 (a batch effect of 0.9 log2 units);
- genes 25–40 are unaffected (noise).

Each gene has its own baseline level (between 6 and 11), and random measurement noise with SD 0.35 log2 units. The generating script (`make_expression.R`, seed 909) is supplied with the Week 9 materials.

Used in Lecture 9 and Workshop 9 (principal component analysis, hierarchical clustering, heatmaps, batch effects).

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/expression.csv", header = TRUE)
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/expression.csv")
```
