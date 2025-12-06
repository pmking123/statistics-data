# biceps.csv Codebook

- **Filename:** `biceps.csv`  
- **Source:** Bulbulian, R., Johnson, R. E., Gruber, J. J., Darabos, B. (1987) "Body Composition in Paraplegic Male Athletes", *Med. Sci. Sports. Exerc*. **19**: 195-201.
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/biceps.csv](https://pmking123.github.io/statistics-data/datasets/biceps.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `group` | factor: 1 = ectomorphic, 2 = mesomorphic, 3 = paraplegic | | Group to which the athlete belonged |
| `circumference`  | numeric | cm | Bicep circumference |

---

## Notes

### Abstract

The body composition and anthropometric characteristics of male paraplegic athletes (PARA, N = 22) were contrasted to an able-bodied ectomorphic (N = 22) and mesomorphic (N = 31) comparison group of moderately and highly trained male subjects. The validity of 12 body composition [density (Db)] prediction equations reported in the literature, 4 generalized, were determined (tested) on this special group of athletes (PARA). On the whole, the prediction equations over-predicted Db in PARA by 0.0039 to 0.0166 g X cm-3 (under-predicted relative fat by 1.8 to 7.4%). Five diameter, 11 circumference, and 7 skinfold measures were used in a SAS-STEPWISE multiple regression procedure with hydrostatically determined Db to develop several suitable Db prediction equations for the paraplegic athlete. Diameters were poor predictors (r = 0.60, SEE = 0.0164), while skinfolds, circumferences, or a combination of measures were acceptable, with the combined equation being best (r = 0.95, SEE = 0.0064). The findings of this study suggest that even generalized equations do not adequately predict Db in PARA and that paraplegic specific equations are presently best suited for predicting Db in paraplegic athletes. The results further indicate that although these equations meet many of the criteria of Lohman, the SEE and total error values are unusually high and make prediction of body composition using anthropometry in a heterogeneous group of PARA athletes slightly unreliable.

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/biceps.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/biceps.csv")
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/biceps.csv")
```
