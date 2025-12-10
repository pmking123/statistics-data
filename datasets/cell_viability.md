# cell_viability.csv Codebook

**Filename:** `cell_viability.csv`  
**Source:** Simulation  
**Purpose in course:** summary statistics, data visualization

---

## Variables

| Variable     | Type     | Description                                                                                          |
|--------------|----------|------------------------------------------------------------------------------------------------------|
| `drug_conc`  | numeric (µM) | Drug concentration of *Inhibitol* applied to the cells, in micromolar (µM). This is the treatment variable expected to affect viability. |
| `replicate`  | integer  | Experimental replicate identifier (1–3). Represents separate runs/plates/days and allows comparison of consistency across replicates. |
| `viability`  | numeric (%) | Measured cell viability expressed as a percentage relative to the untreated control. This is the biological response variable. |

---

## Notes


---

## Example usage

### In R

```r
df <- read.csv("cell_viability.csv", header = TRUE)
```

### In Python

```python
import pandas as pd
df = pd.read_csv("cell_viability.csv")
```
