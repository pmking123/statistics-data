# biomarker.csv Codebook

- **Filename:** `biomarker.csv`  
- **Source:** simulated data
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/biomarker.csv](https://pmking123.github.io/statistics-data/datasets/biomarker.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `treatment` | factor: 0 = placebo, 1 = drug | | Treatment received by trial participant. |
| `sex`  | factor: 0 = female, 1 = male |  | Sex of trial participant |
| `biomarker`    | numeric            | arbitrary  | Biomarker concentration |


---

## Notes

As part of an investigation into a novel therapeutic treatment, equal numbers of men and women were recruited for a clinical trial. Exactly half of each group were given the novel treatment, while the other half were given a placebo. After four weeks, the concentration of a specific biomarker was measured in each individual trial participant.

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/biomarker.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/biomarker.csv")
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/biomarker.csv")
```
