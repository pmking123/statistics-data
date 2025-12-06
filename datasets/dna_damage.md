# dna_damage.csv Codebook

- **Filename:** `dna_damage.csv`  
- **Source:** Schurdak, M. E. and Randerath, K. (1989) "Effects of Route of Administration on Tissue Distribution of DNA Adducts in Mice: Comparison of 7,H-Dibenzo(c,g)carbazole, Benzo(a)pyrine, and 2-Acetylaminofluorene", *Cancer Res*. **49**: 2633-2638.
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/dna_damage.csv](https://pmking123.github.io/statistics-data/datasets/dna_activity.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `damage` | numeric | arbitrary units | Carcinogenicity (DNA damage) |
| `carcinogen`  | factor: 1 = benzo(*a*)pyrine, 2 = dibenzo(*c,g*)carbazole, 3 = acetylaminofluorene | | Carcinogen administered |
| `route`  | factor: 1 = topical, 2 = oral, 3 = subcutaneous |  | Mode of administration |
| `tissue`  | factor: 1 = liver, 2 = kidney, 3 = lung, 4 = skin |  | Damaged tissue |

---

## Notes

### Abstract

7H-Dibenzo[c,g]carbazole (DBC) is a potent liver and skin carcinogen following topical administration. The objective was to determine the pattern of DBC-DNA adducts produced in both target and nontarget tissues when DBC and its metabolites were applied topically at carcinogenic doses. DBC phenolic derivatives 1-hydroxy-DBC, 2-hydroxy-DBC, 3-hydroxy-DBC, 4-hydroxy-DBC, 5-hydroxy-DBC, 6-hydroxy-DBC, 13-c-hydroxy-DBC, and N-methyl-DBC were applied dermally to Hsd:ICR (Br) mice. Tissues were harvested 24 h later, and DBC-DNA adduct levels were determined by 32P-postlabeling. The levels of DBC-DNA adducts were about 25 times greater in liver than in any other tissue. Total DBC-DNA adducts were seen in skin and lung at about equal levels, while adduct levels in kidney and other tissues were no more than one fourth that of lung and skin. Adduct 6 was the predominant adduct in liver, adducts 2 and 3 were formed preferentially in skin, and adduct 3 was formed preferentially in lung. 3-Hydroxy-DBC and 4-hydroxy-DBC produced higher levels of DNA adducts in skin, lung, and liver than did the parent compound or 2-hydroxy-DBC. DNA adducts were not seen in any tissue for the 1-, 5-, 6-, or 13-c-hydroxy compounds. In addition, hepatic DNA adducts were not seen when the nitrogen of DBC was methylated. In lung and skin, N-methyl-DBC induced DNA adducts at levels comparable to DBC, although the adduct profile in these tissues was different from that of DBC itself.

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/dna_damage.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/dna_damage.csv")
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/dna_damage.csv")
```
