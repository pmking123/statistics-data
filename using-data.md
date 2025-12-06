# Using the statistics-data datasets

This page explains how to load the datasets into **R**, **Python**, and **Excel**.

All datasets are available via short URLs like:

```
https://pmking123.github.io/statistics-data/datasets/FILENAME.csv
```

---

## 1. R

```r
url <- "https://pmking123.github.io/statistics-data/datasets/FILENAME.csv"
dat <- read.csv(url)
head(dat)
```

Save a local copy:

```r
download.file(url, "FILENAME.csv", mode = "wb")
```

---

## 2. Python (pandas)

```python
import pandas as pd
df = pd.read_csv("https://pmking123.github.io/statistics-data/datasets/FILENAME.csv")
df.head()
```

---

## 3. Excel

### Option A — Direct download  
Navigate to the dataset in the Pages site and download the CSV.

### Option B — *Data → From Web*
Paste any dataset URL, such as:

```
https://pmking123.github.io/statistics-data/datasets/BOD.csv
```

---

## 4. Codebooks

For each dataset:

```
datasets/BOD.csv
datasets/BOD.md
```

The `.md` file contains variable definitions, units, missing value notes, and examples.

---

## 5. Good practice in scripts

Always record:

- the dataset URL  
- the date accessed  
- a short description of the dataset

Example (R):

```r
# Data: BOD (biochemical oxygen demand)
url <- "https://pmking123.github.io/statistics-data/datasets/BOD.csv"
bod <- read.csv(url)
```

Example (Python):

```python
url = "https://pmking123.github.io/statistics-data/datasets/iris.csv"
iris = pd.read_csv(url)
```

---
