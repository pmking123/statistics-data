# dna_activity.csv Codebook

- **Filename:** `dna_activity.csv`  
- **Source:** Belury, M. A., Patrick, K. E., Locniskar, M. and Fischer, S. M. (1989) "Eicosapentaenoic and Arachidonic Acid: Comparison of Metabolism and Activity in Murine Epidermal Cells". *Lipids* **24**:423-429.
- **Data repository:** [https://pmking123.github.io/statistics-data/datasets/dna_activity.csv](https://pmking123.github.io/statistics-data/datasets/dna_activity.csv)

---

## Variables

| Variable | Type (numeric / factor / character / date) | Units | Description |
|---------|---------------------------------------------|-------|-------------|
| `acid` | factor: 1 = arachidonic acid, 2 = eicosapentaenoic acid | | Presence of fatty acid in cell culture |
| `tpa`  | factor: 0 = absent, 1 = present | | Presence or absence of 12-O-tetradecanoylphorbol-13-acetate in the cell culture |
| `activity`  | numeric | arbitrary | Specific activity of DNA synthesis |

---

## Notes

### Abstract

The biological activity, including metabolism and modulation of ornithine decarboxylase activity and DNA synthesis, of arachidonic acid (AA) and eicosapentaenoic acid (EPA) were compared in epidermal cells from SENCAR mice. Radiolabelled AA and EPA were found to be similarly incorporated into and released from membrane phospholipids of unstimulated cultures. However, when cells were stimulated with the tumor promoter 12-0-tetradecanoylphorbol-13-acetate (TPA), the release of AA was significantly higher than the release of EPA. The extent of metabolism of AA and EPA to prostaglandins was determined in both freeze-thawed cell preparations and in viable cultured cells. In the freeze-thawed preparations, use of AA as a substrate resulted in significantly more PGF than when EPA was used as the substrate. However, more PGE3 was formed than PGE2. PGD levels were the same for either fatty acid precursor. Prostaglandin production was also determined in viable cultured cells since other influences such as phospholipase A2 activity can modify prostaglandin production. Control cultures prelabelled with either AA or EPA produced similar amounts of the respective PGF, PGE, and PGD. However, TPA-stimulated cultures produced significantly higher amounts of each prostaglandin in cultures prelabelled with AA compared to cells prelabelled with EPA. HETE or HEPE production was the same both for cultured cells prelabelled with AA or EPA and for homogenates from uncultured cells incubated directly with the radiolabelled fatty acids. TPA-induced ornithine decarboxylase (ODC) was significantly higher in AA-treated cultures compared to EPA-treated cultures. AA supports DNA synthesis to a greater extent than EPA, either alone or in the presence of TPA. These findings suggest that AA and EPA do not have equivalent biological activity in mouse epidermal cells.

---

## Example usage

### In R

```r
df <- read.csv("https://pmking123.github.io/statistics-data/datasets/dna_activity.csv", header = TRUE)
```

or

```r
library(readr)
df <- read_csv("https://pmking123.github.io/statistics-data/datasets/dna_activity.csv")
```

### In Python

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/dna_activity.csv")
```
