# saliva.csv Codebook

- **Filename:** `saliva.csv`  
- **Source:** Johnson, D. A. and Cortez, J. E. (1988) "Chronic Treatment with Beta Adrenergic Agonists and Antagonists Alters the Composition of Proteins in Rat Parotid Saliva". *J. Dent. Res.* **67**: 1103-1108.
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/saliva.csv](https://pmking123.github.io/statistics-data/datasets/saliva.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `group` | factor: 1 = control, 2 = isoproterenol, 3 = dobutamine, 4 = terbutaline, 5 = metoprolol | | Group to which the athlete belonged |
| `protein`  | numeric | mg / mL | Proline-rich protein content of saliva |

---

## Notes

### Abstract

This investigation was undertaken to determine the role of β-adrenergic receptors in the regulation of the protein composition of rat parotid saliva. Chronic treatment of rats with dobutamine, a β1-adrenergic agonist, resulted in changes in parotid saliva volume, protein concentration, and composition which were essentially the same as those changes which occurred following chronic treatment with isoproterenol, a non-specific β-adrenergic agonist. Chronic treatment with the β2-adrenergic agonist, terbutaline, had no effect on parotid saliva volume, protein concentration, or composition. Chronic treatment of rats with a β1-adrenergic antagonist, metoprolol, had different effects on saliva dependent on the manner by which the drug was delivered. Twice-daily injections of metoprolol led to a decrease in flow rate, but protein concentration and composition were unaltered. When metoprolol was delivered by surgically implanted osmotic mini pumps, neither the flow of parotid saliva nor its concentration of protein was altered; however, there was a reduction in the proportion of proline-rich proteins in saliva. Comparable changes in parotid saliva protein composition occurred when the mini pumps delivered propranolol, a non-specific β-adrenergic antagonist. Chronic treatment of rats with an α2-adrenergic agonist (clonidine) or antagonist (yohimbine) was without effect on parotid saliva flow rate, protein concentration, or composition. These findings suggest that the synthesis of proline-rich proteins is regulated, in part, by β-adrenergic receptor stimulation, and primarily by the β1-receptor subtype.

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/saliva.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/saliva.csv")
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/saliva.csv")
```
