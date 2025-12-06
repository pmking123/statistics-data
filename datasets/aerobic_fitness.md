# aerobic_fitness.csv Codebook

- **Filename:** `aerobic_fitness.csv`  
- **Source:** simulated data
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/aerobic_fitness.csv](https://pmking123.github.io/statistics-data/datasets/aerobic_fitness.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `ID`   | numeric| | Participant number |
| `VO2_max`   | numeric | ml kg^-1^ min^-1^ | Maximal oxygen consumption, VO₂max |
|`Exercise_Hours`    |      numeric            | hours  | Weekly exercise |
|`RHR`    |      numeric            | beats per minute  | Resting heart rate |

---

## Notes

A research team wants to understand what predicts aerobic fitness in adults. They want to determine whether adding Resting Heart Rate to the model improves prediction of VO₂max compared with using Exercise Hours alone.

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/aerobic_fitness.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/aerobic_fitness.csv")
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/aerobic_fitness.csv")
```
