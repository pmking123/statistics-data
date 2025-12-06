# esbl.csv Codebook

- **Filename:** `esbl.csv`  
- **Source:** simulated data
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/esbl.csv](https://pmking123.github.io/statistics-data/datasets/esbl.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `ESBL`         | factor: 0 = no, 1 = yes | | Isolate ESBL-producing |
| `AB_EXPOSURE`  | numeric | days | number of days of broad-spectrum antibiotic therapy in the last 30 days |
| `HOSP_DAYS`    | numeric            | days  | Total length of hospital stay (days) up to the date of sampling |
| `ICU`          | factor: 0 = not admitted, 1 = admitted| beats per minute  | Admitted to ICU at any time during stay |
| `URINE_SAMPLE` | factor: 0 = non-urine sample, 1 = urine sample |  | Sample source |

---

## Notes

A hospital microbiology lab collected data on a number of *E. coli* isolates from inpatients.  For each isolate, they recorded whether it produced extended-spectrum β-lactamases (ESBL) and several potential risk factors.

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/esbl.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/esbl.csv")
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/esbl.csv")
```
