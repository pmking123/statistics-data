# kidney.csv Codebook

- **Filename:** `kidney.csv`  
- **Source:** E. W. Lipkin, S. M. Ott, C. H. Chesnut III and A. Chait, "Mineral Loss in the Parenteral Nutrition Patient", *Am. J. Clin. Nutr.* 47:515-523, 1988.
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/kidney.csv](https://pmking123.github.io/statistics-data/datasets/kidney.csv)

---

## Variables

Fill in one row per column in `kidney.csv`.

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `uca`   |      numeric            |   mg / 12 h    |      Urinary Ca^2+^ |
| `dca`   |      numeric            |   mg / 12 h    |      Dietary Ca^2+^ |
|`gfr`    |      numeric            |   mL / min   |      Glomerular filtration rate |
|`una`   |      numeric            |   mEq / 12 h    |      Urinary Na^+^ |
|`dp`|        numeric            |   g / day    |      Dietary protein |

---

## Notes

None

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/kidney.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/kidney.csv")
```


### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/kidney.csv")
```
