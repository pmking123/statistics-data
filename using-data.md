# Using the statistics-data datasets

This page explains how to load the datasets from this repository into R, Python, and Excel.

The data are hosted via **GitHub Pages**, so every dataset can be accessed with a short web URL of the form

```text
https://pmking123.github.io/statistics-data/datasets/<filename>
```

For example:

```text
https://pmking123.github.io/statistics-data/datasets/BOD.csv
https://pmking123.github.io/statistics-data/datasets/iris.csv
```

You normally **do not need to download files manually** – you can load them directly from these URLs in R or Python.

---

## 1. Using the data in R

Make sure you have an internet connection when you run the code.

### 1.1 Loading a single dataset

Replace `FILENAME.csv` with the dataset you want, e.g. `BOD.csv` or `iris.csv`:

```r
url <- "https://pmking123.github.io/statistics-data/datasets/FILENAME.csv"
dat <- read.csv(url, header = TRUE)

# Check the first few rows
head(dat)
str(dat)
```

### 1.2 Saving a local copy

If you want to keep a local copy so that you can work offline:

```r
url  <- "https://pmking123.github.io/statistics-data/datasets/FILENAME.csv"
path <- "FILENAME.csv"   # or any local path you prefer

download.file(url, destfile = path, mode = "wb")
dat <- read.csv(path)
```

---

## 2. Using the data in Python (pandas)

First install pandas if needed (`pip install pandas`), then:

```python
import pandas as pd

url = "https://pmking123.github.io/statistics-data/datasets/FILENAME.csv"
df = pd.read_csv(url)

print(df.head())
print(df.info())
```

As in R, you can replace `FILENAME.csv` with any dataset in the `datasets/` folder.

To save a local copy:

```python
import pandas as pd

url = "https://pmking123.github.io/statistics-data/datasets/FILENAME.csv"
df = pd.read_csv(url)

df.to_csv("FILENAME.csv", index=False)
```

---

## 3. Using the data in Excel

1. Go to  
   `https://pmking123.github.io/statistics-data/`
2. Navigate to the `datasets/` folder.
3. Click the CSV you want.
4. Use your browser’s **Download** option (or right‑click → “Save link as…”).
5. Open the downloaded `.csv` file in Excel.

Alternatively, in newer versions of Excel you can use:

- **Data → From Web** and paste the dataset URL, e.g.  
  `https://pmking123.github.io/statistics-data/datasets/BOD.csv`

---

## 4. Codebooks (variable descriptions)

For most datasets there is a matching **Markdown codebook** that explains each variable, units, and any coding schemes.

- If the data file is `datasets/BOD.csv`, the codebook is typically `datasets/BOD.md`.
- You can read these directly on the GitHub repository or via GitHub Pages, e.g.  
  `https://pmking123.github.io/statistics-data/datasets/BOD.md`

Before analysing a dataset, **always** check its codebook to understand what the variables represent.

---

## 5. Reproducible scripts

When you write scripts for assignments or lab work, it is good practice to:

1. Include the URL you used to load the data.
2. Mention the date you downloaded it (if you saved a local copy).
3. Add a short comment with the dataset name / context.

Example in R:

```r
# Data: BOD.csv from statistics-data repository
url <- "https://pmking123.github.io/statistics-data/datasets/BOD.csv"
bod <- read.csv(url)
```

Example in Python:

```python
# Data: iris.csv from statistics-data repository
url = "https://pmking123.github.io/statistics-data/datasets/iris.csv"
iris = pd.read_csv(url)
```

This makes it easy for someone else (or future‑you) to reproduce your analysis.
