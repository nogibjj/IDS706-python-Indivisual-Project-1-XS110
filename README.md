

# IDS 706 Individual Project 1


## Data

The data is from kaggle [world population](https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset). In this Dataset, we have Historical Population data for every Country/Territory in the world by different parameters like Area Size of the Country/Territory, Name of the Continent, Name of the Capital, Density, Population Growth Rate, Ranking based on Population, World Population Percentage, etc.

I downloaded `word_population.csv` from kaggle and uploaded it into this resporitory.

## Setup

I used week3 mini project as a template and made the following modifications: 

### 1. Update requirements.txt:
```
#script
nbval
ruff
```
### 2. jupyter notebook

I created `individual_project.ipynb` to perform descriptive statistics using Polars

### 3. .py file

I created two .py files and save them in scripts folder

1. `script.py`
2. `lib.py`

### 4. test_.py file

I created two test_.py files to test the Python script and library, and save them in scripts folder

1. `test_script.py`
2. `test_lib.py`

The test_script.py tests script.py runs without errors, and test_lib.py tests each functions in lib.py
 

### 5. Update Makefile

The Makefile correctly includes and executes all required commands.

Running all tests (notebook, script, lib)
```
test:
	python -m pytest -vv --cov=scripts scripts/test_*.py
	pytest --nbval individual_project.ipynb
```

Formatting code with Python black	
```
format:
	black scripts/*.py
```

Linting code with Ruff
```
lint:
	ruff check scripts/*.py
```

## Results

### Github Actions badges

[![install](https://github.com/nogibjj/IDS706-python-Indivisual-Project-1-XS110/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706-python-Indivisual-Project-1-XS110/actions/workflows/install.yml)

[![lint](https://github.com/nogibjj/IDS706-python-Indivisual-Project-1-XS110/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IDS706-python-Indivisual-Project-1-XS110/actions/workflows/lint.yml)

[![format](https://github.com/nogibjj/IDS706-python-Indivisual-Project-1-XS110/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IDS706-python-Indivisual-Project-1-XS110/actions/workflows/format.yml)

[![test](https://github.com/nogibjj/IDS706-python-Indivisual-Project-1-XS110/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706-python-Indivisual-Project-1-XS110/actions/workflows/test.yml)

[![generate_report](https://github.com/nogibjj/IDS706-python-Indivisual-Project-1-XS110/actions/workflows/generate_report.yml/badge.svg)](https://github.com/nogibjj/IDS706-python-Indivisual-Project-1-XS110/actions/workflows/generate_report.yml)

### Report

I automatically generate the descriptive statistics report to `report.md`. 

### Demo Video



## Data Visualization

I analysed the 234 countries' population in 2022, growth rate and Area(km²).

### 1. Summary statistics using the describe method

![Alt text](/image/image1.png)

### 2. Mean, Median and Mode

![Alt text](/image/image2.png)

### 3. Variance and standard deviation

![Alt text](/image/image3.png)

### 4. histogram of 2022 population

![Alt text](/image/population_histogram.png)

### 5. boxplot of 2022 population

![Alt text](/image/population_boxplot.png)