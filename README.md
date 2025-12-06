# statistics-data

This repository contains datasets used across statistics modules.  
All datasets are provided as **clean data files** with no embedded metadata.  
Each dataset has a matching **Markdown codebook** describing variables, units, and notes.

---

## 📚 How the documentation is organised

- Miscellaneous datasets are contained in the `datasets/` folder.
- For each dataset file like `BOD.csv` there is a corresponding codebook, e.g. `BOD.md`.
- Codebooks live alongside the data files in the same folder.
- Textbook-specific datasets are stored in the `textbook_data/` folder, in various subfolders:
  - `Barton_Peat/`
  - `Discovering_Statistics/`
  - `Getting_Started_in_Statistics/`
  - `Glantz-Slinker/`
  - `Grafen_and_Hails/`
  - `Hawkins_Biomeasurement_3e/`
  - `Hawkins_Biomeasurement_4e/`
  - `OpenIntro/`
  - `Samuels_Witmer/`
  - `Samuels_Witmer_4e/`

---

## 🔎 Classic / demonstration datasets

These are “textbook classics” often used to illustrate basic statistical ideas.

| Dataset | Brief description | Codebook |
|---------|-------------------|----------|
| `Anscombe_1.csv` | Anscombe's quartet – set 1 (regression diagnostics) | `Anscombe_1.md` |
| `Anscombe_2.csv` | Anscombe's quartet – set 2 | `Anscombe_2.md` |
| `Anscombe_3.csv` | Anscombe's quartet – set 3 | `Anscombe_3.md` |
| `Anscombe_4.csv` | Anscombe's quartet – set 4 | `Anscombe_4.md` |
| `iris.csv` | Fisher's iris data – classic 3-species classification | `iris.md` |
| `ChickWeight.csv` | Chick growth under different diets (longitudinal) | `ChickWeight.md` |
| `chickwts.csv` | Chick weights by feed type | `chickwts.md` |
| `InsectSprays.csv` | Effectiveness of insect sprays (counts) | `InsectSprays.md` |
| `OrchardSprays.csv` | Pest control in orchards | `OrchardSprays.md` |
| `PlantGrowth.csv` | Plant weights under different treatments | `PlantGrowth.md` |
| `ToothGrowth.csv` | Tooth growth in guinea pigs by dosage | `ToothGrowth.md` |
| `pressure.csv` | Vapor pressure of mercury vs temperature | `pressure.md` |
| `women.csv` | Heights and weights of women | `women.md` |
| `Davis.csv` | Self-reported vs measured heights/weights | `Davis.md` |
| `bdims.csv` | Body dimensions (anthropometry) | `bdims.md` |

---

## 🌱 Environmental / ecological / biological datasets

| Dataset | Brief description | Codebook |
|---------|-------------------|----------|
| `BOD.csv` | Biochemical oxygen demand over time | `BOD.md` |
| `CO2.csv` | CO₂ uptake in plants under varying conditions | `CO2.md` |
| `ChickWeight.csv` | Chick growth under different diets | `ChickWeight.md` |
| `chickwts.csv` | Chick weights by feed type | `chickwts.md` |
| `DNase.csv` | Enzymatic activity vs concentration | `DNase.md` |
| `Formaldehyde.csv` | Formaldehyde concentration data | `Formaldehyde.md` |
| `growth.csv` | Growth curves (specify context in codebook) | `growth.md` |
| `limpet.csv` | Limpet-related ecological data | `limpet.md` |
| `metals.csv` | Environmental metal concentrations | `metals.md` |
| `Soils.csv` | Soil properties | `Soils.md` |
| `ozone.csv` | Ozone measurements over time/space | `ozone.md` |
| `reeds.csv` | Plant or habitat data on reeds | `reeds.md` |

---

## 🧬 Biomedical / clinical datasets

| Dataset | Brief description | Codebook |
|---------|-------------------|----------|
| `CK.csv` | Creatine kinase / enzyme activity data | `CK.md` |
| `COHb.csv` | Carboxyhaemoglobin measurements | `COHb.md` |
| `MAO.csv` | Monoamine oxidase activity | `MAO.md` |
| `PBCD_F.XPT` | NHANES or similar clinical data (SAS xport) | `PBCD_F.md` |
| `WeightLoss.csv` | Weight loss study data | `WeightLoss.md` |
| `anorexia.csv` | Anorexia treatment data | `anorexia.md` |
| `bladder.csv` | Bladder cancer recurrence data | `bladder.md` |
| `bone_density.csv` | Bone mineral density | `bone_density.md` |
| `cdc.csv` | CDC sample survey data | `cdc.md` |
| `chorioamnion.csv` | Chorioamnionitis or related obstetric data | `chorioamnion.md` |
| `cortisol.csv` | Cortisol levels over time / treatments | `cortisol.md` |
| `cystfibr.csv` | Cystic fibrosis-related data | `cystfibr.md` |
| `diets.csv` | Diet comparison study | `diets.md` |
| `fev1_weaning_single_dataset.csv` | Lung function (FEV1) and weaning | `fev1_weaning_single_dataset.md` |
| `hormone.csv` | Hormone levels vs treatment/time | `hormone.md` |
| `hypertensive_dogs.csv` | Blood pressure in hypertensive dogs | `hypertensive_dogs.md` |
| `infert.csv` | Infertility and treatments data | `infert.md` |
| `insulin.csv` | Insulin measurements | `insulin.md` |
| `intravenous.csv` | Intravenous infusion / pharmacokinetics | `intravenous.md` |
| `kidney.csv` | Kidney function data | `kidney.md` |
| `normal_dogs.csv` | Baseline measurements in normal dogs | `normal_dogs.md` |
| `permeability.csv` | Membrane / vascular permeability | `permeability.md` |
| `plasma.csv` | Plasma concentration data (PK/PD) | `plasma.md` |
| `protein_metabolism.csv` | Protein metabolism study | `protein_metabolism.md` |
| `red_cell_folate.csv` | Red cell folate levels | `red_cell_folate.md` |
| `retinal_permeability.csv` | Retinal permeability measurements | `retinal_permeability.md` |
| `sickle.csv` | Sickle-cell related data | `sickle.md` |
| `sleep.csv` | Sleep study data | `sleep.md` |
| `stress.csv` | Stress measurements (e.g. cortisol, HR) | `stress.md` |
| `toxic_shock.csv` | Toxic shock syndrome data | `toxic_shock.md` |

---

## 👶 Demographic / social / survey datasets

| Dataset | Brief description | Codebook |
|---------|-------------------|----------|
| `age_waist.csv` | Age and waist measurements | `age_waist.md` |
| `arbuthnot.csv` | Arbuthnot's historical birth data | `arbuthnot.md` |
| `birth_weight.csv` | Birth weights and covariates | `birth_weight.md` |
| `births.csv` | Birth counts / characteristics | `births.md` |
| `birthweight.csv` | Neonatal birthweight data | `birthweight.md` |
| `birthwt.csv` | Low birth weight and risk factors | `birthwt.md` |
| `blood_eye.csv` | Blood type and eye colour | `blood_eye.md` |
| `compensation.csv` | Compensation / salary study | `compensation.md` |
| `energy.csv` | Energy usage survey | `energy.md` |
| `height.csv` | Height data | `height.md` |
| `martian.csv` | “Martian” data (typically toy example) | `martian.md` |
| `maths.csv` | Mathematics scores / attitudes | `maths.md` |
| `present.csv` | Time series of presents / sales (toy) | `present.md` |
| `type1.csv` | Type I error illustration dataset | `type1.md` |
| `ukwcs_regression.csv` | UKWCS regression dataset | `ukwcs_regression.md` |
| `ukwcs_regression_diet.csv` | Diet variables for UKWCS regression | `ukwcs_regression_diet.md` |
| `whr.csv` | Waist–hip ratio data | `whr.md` |
| `womensrole.csv` | Attitudes towards women’s roles | `womensrole.md` |

---

## 📈 Regression / designed experiment / other modelling datasets

| Dataset | Brief description | Codebook |
|---------|-------------------|----------|
| `ICE1_SAT1.csv` | In-class SAT/ICE exercise | `ICE1_SAT1.md` |
| `In_class_exercise_1.csv` | In-class exercise data | `In_class_exercise_1.md` |
| `Lambs.csv` | Lamb growth / treatment study | `Lambs.md` |
| `Leinhardt.csv` | Income and infant mortality | `Leinhardt.md` |
| `MAO.csv` | Monoamine oxidase activity | `MAO.md` |
| `edta_atomic.csv` | EDTA titration / atomic analysis | `edta_atomic.md` |
| `esoph.csv` | Esophageal cancer case–control data | `esoph.md` |
| `figure_3.7.csv` | Data for textbook Figure 3.7 | `figure_3.7.md` |
| `leaflet-game.csv` | Leaflet game experiment | `leaflet-game.md` |
| `metallothionein.csv` | Metallothionein expression data | `metallothionein.md` |
| `ozone.csv` | Ozone data (also time series) | `ozone.md` |
| `roberts.csv` | Study data from Roberts et al. | `roberts.md` |
| `sleep.csv` | Sleep deprivation experiment | `sleep.md` |
| `two-way-regression.csv` | Two-way regression example | `two-way-regression.md` |
| `two-way-regression.xlsx` | Same data in Excel form | `two-way-regression.md` |

---


## 💻 Loading data

### In R

```r
df <- read.csv("filename.csv", header = TRUE)
```

### In Python (pandas)

```python
import pandas as pd
df = pd.read_csv("filename.csv")
```

### In Excel

On GitHub, click the file → **Download raw**.

---

## 🧭 Conventions

- CSV files contain **raw data only**, with no comments or explanatory text.
- Variable names and explanations live in the corresponding `*.md` codebook.
- Folder-level `README.md` files summarise the datasets from each textbook collection.

---

## 📄 License

These datasets are provided for educational use in statistics courses.
