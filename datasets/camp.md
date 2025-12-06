# camp.csv Codebook

- **Filename:** `camp.csv`  
- **Source:** Yoshida, H., Oshima, H., Saito, E. and Kinoshita, M. (1988) "Hyperparathyroidism in Patients with Myotonic Dystrophy". *J. Clin. Endocrinol. Metab.* **67**: 488-492.
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/camp.csv](https://pmking123.github.io/statistics-data/datasets/camp.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `group` | factor: 1 = control, 2 = myotonic dystrophy, 3 = nonmyotonic dystrophy | | Group of patient |
| `cAMP`  | numeric | nmol / dl | renal excretion of cAMP |



---

## Notes

### Abstract

This study was designed to determine the possible presence of abnormal calcium metabolism in patients with myotonic dystrophy (MyD). Twenty-five patients with MyD, 13 patients with other neuromuscular disorders (non-MyD), and 12 normal subjects were studied. The mean plasma 1,25-dihydroxy-vitamin D level in the MyD patients [83.2 ± 23.1 (±sd) pmol/L] was significantly higher than those in the other two groups [normal subjects, 49.7 ± 15.4 (P < 0.01); non-MyD patients, 51.6 ± 27.4 (P < 0.01)]. On the contrary, the mean plasma 24,25-dihydroxyvitamin D levels were similar in the MyD patients and the normal subjects. The increments in serum calcium levels and urinary calcium excretion after oral calcium loading in the MyD patients were significantly greater than those in the normal subjects, suggesting that intestinal calcium absorption was augmented in the MyD patients. The mean nephrogenous cAMP excretion in the MyD patients (1.71 ± 1.08 nmol/100 mL glo-merular filtrate) also was higher than those in the other two groups (0.93 ± 0.34 in the non-MyD patients; 0.91 ± 0.21 in normal subjects). These results suggest that parathyroid function may be increased in MyD patients.

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/camp.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/camp.csv")
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/camp.csv")
```
