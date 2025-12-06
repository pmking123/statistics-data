# water.csv Codebook

- **Filename:** `water.csv`  
- **Source:** 
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/water.csv](https://pmking123.github.io/statistics-data/datasets/water.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `town`   | character | |Name of the town |
| `location`   | factor: "N" = North, "S" = South | | Location of the town |
|`mortality`    |      numeric            |   | Male mortality rate per 100,000 |
|`hardness`    |      numeric            | ppm  | Calcium concentration in drinking water |

---

## Notes

As part of an investigation into environmental factors which influence public health, a study was undertaken to examine the influence of water hardness upon mortality rates in different towns within the UK.

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/water.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/water.csv")
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/water.csv")
```
