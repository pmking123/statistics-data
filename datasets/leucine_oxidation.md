# leucine_oxidation.csv Codebook

- **Filename:** `leucine_oxidation.csv`  
- **Source:** Hood, D. A. and Terjung, R. L. (1987) "Effect of Endurance Training on Leucine Metabolism in Peerfused Rat Skeletal Muscle". *Am. J. Physiol.* **253**: E648-656.
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/leucine_oxidation.csv](https://pmking123.github.io/statistics-data/datasets/leucine_oxidation.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `subject` | numeric |  | Identifier for matched pairs of rats |
| `stimulation`  | factor: 0 = 0, 1 = 15, 2 = 45 | per min | Stimulation regime (contraction frequency) |
| `training`  | factor: 1 = trained, 2 = untrained |  | Training regime of rat |
| `leucine`  | numeric | % | Leucine oxidation contribution to energy needs |

---

## Notes

### Abstract

An isolated single rat hindlimb muscle preparation was used to examine the influence of exercise training on leucine metabolism during steady-state conditions at rest and during isometric contractions. Treadmill training increased the activity of citrate synthase in the hindlimb muscle by 40-45%. Leucine oxidation, measured as the rate of alpha-decarboxylation, was not different between trained (2.28 ± 0.15 nmol min-1 g-1, n = 9) and control (2.57 ± 0.20, n = 9) muscle at rest. In addition, successive 40-min contraction periods at 15 and 45 tetani/min induced similar increases (50 and 100%, respectively) in leucine oxidation in both groups. However, trained muscle maintained a greater tension output (P less than 0.05) during contractions and exhibited a greater oxygen consumption (VO2) (P less than 0.05) during 45 tetani/min. Thus the rate of leucine oxidation, relative to VO2, was less (P less than 0.05) in the trained group. This response was probably related to differences in intracellular factors modulating branched-chain alpha-keto acid dehydrogenase, the rate-limiting step in leucine oxidation. Although our observed rates of muscle leucine alpha-decarboxylation can reasonably account for the rates of whole-body leucine alpha-decarboxylation of nontrained individuals found during steady-state tracer studies in vivo, this is less reasonably the case for the trained group. This suggests that a greater rate of leucine oxidation by nonmuscle tissues (e.g., liver) may occur in trained compared with nontrained individuals.

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/leucine_oxidation.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/leucine_oxidation.csv")
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/leucine_oxidation.csv")
```
