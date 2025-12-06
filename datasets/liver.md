# liver.csv Codebook

- **Filename:** `liver.csv`  
- **Source:** 
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/liver.csv](https://pmking123.github.io/statistics-data/datasets/liver.csv)

---

## Variables

Fill in one row per column in `liver.csv`.

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `Age`   |      numeric            |   years   |  Age of patient in years |
| `Gender`   |      Factor: "Female", "Male"   |      |     Sex of patient |
|`Total_Bilirubin`    |      numeric            |   mg / dl   |      Total bilirubin |
|`Direct_Bilirubin`   |      numeric            |   mg / dl    |     Direct bilirubin |
|`Alkaline_Phosphatase`|        numeric            |   IU / L    |  Alkaline phosphatase (ALP) |
|`Alanine_Aminotransferase`|        numeric            |   IU / L    | Alanine aminotransferase (ALT) |
|`Aspartate_Aminotransferase`|        numeric            |   IU / L  | Aspartate aminotransferase (AST) |
|`Total_Protein`|        numeric            |   g / dl    |      Total protein |
|`Albumin`|        numeric            |   g / dl    |      Albumin |
|`Albumin_and_Globulin_Ratio`|        numeric            |     | Albumin to globulin ratio (A/G) |

---

## Notes

None

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/liver.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/liver.csv")
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/liver.csv")
```
