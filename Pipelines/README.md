# Modular Data Cleaning & Visualization Pipeline
A modular Python tool for loading, cleaning, imputing, and visualizing datasets across multiple file formats via a command-line interface (CLI).

## Introduction

This pipeline automates dataset loading, preprocessing, and exploratory data analysis (EDA). Built with modular design principles, the project breaks down raw data ingestion, missing value imputation, feature categorization, and visual analysis into reusable Python scripts. It also saves the cleaned file into a directory of choice as a csv.


## Key Capabilities

- Multi-Format Ingestion: Supports .csv, .xlsx, .json, .parquet, .txt, and .tsv files.

- Automated Data Cleaning: Removes duplicate rows and imputes missing numeric values with the median and missing categorical values with the mode.

- Dynamic Feature Detection: Automatically segregates numeric and categorical columns for tailored preprocessing and visualization.

- Publication-Ready Visualizations: Generates scatter plot matrices (SPLOM) for continuous features and clean count distributions for categorical features with zero hardcoded visual parameters.

- CLI Integration: Accepts flexible command-line arguments to specify input source files and output destinations.

## How to Clone the Repository
You have to first have Git installed on your machine to get started. If you don't have this, open up your terminal and run:
- On Windows:
```bash
$ winget install --id Git.Git -e --source winget
```
- On Mac:
```bash
$brew install git
```

To clone this repository to your local machine, run the following from a terminal:

```bash
$ git clone https://github.com/dqjohnson/umich.git
```

Then, navigate to the Pipelines folder:

```bash
$ cd umich/Pipelines
```

To check the git status, you can run the following:
```bash
$ git status
```

## Environment Setup & Requirements
### Prerequisites
You must have [python](https://www.python.org/) installed to use these scripts.

Python 3.10 or higher (tested on Python 3.14)

#### Install Required packages:

The requirements.txt file has all packages and versions required to run these scripts using the [pip package manager](https://pypi.org/project/pip/). 
```bash
$ python -m pip install -r requirements.txt
```

## Scripts and Functionality 
### main.py
This is the CLI entry point for running the pipeline. Serves as the command-line interface using argparse. It accepts mandatory input and output file paths from the user, orchestrates data loading, triggers cleaning routines, and launches visual plots.

### clean_data.py
Handles data cleaning by dropping exact duplicate rows, imputing missing numerical values using column medians, imputing missing categorical values using column modes, and exporting the cleaned dataset to the specified output destination. Saves the cleaned file to a `.csv`.

### load_data.py
Extracts file extensions dynamically and reads a dataset into a Pandas DataFrame. Supported multiple formats, including `CSV`, `Excel (.xlsx)`, `JSON`, `Parquet`, `TXT`, and `TSV`. 

### get_data_types.py
Provides utility functions, `numeric_cols()` and `categorical_cols()`, to filter and separate DataFrame columns based on their data types.

### visualize.py
Contains plotting functions:
- `scatter_splom()` Creates a scatter plot matrix (SPLOM) with histograms along the diagonal for numeric features.
- `categorical_distributions_plot()` Creates side-by-side count plots for categorical features.

## Data File Setup
Once you clone the github repository, it will automatically be given two sample datasets, located in the folder `\data`.  However, if you chose to add your own datasets, you can add them anywhere.  You will just need to specify the path per the examples of how to run the code below.  

## How to Run
Run the `main.py` script from your terminal by passing the input file path followed by your desired cleaned output file path:

- Format: `python main.py <input_file> <output_file>`

### Examples:
Processing a CSV dataset:
```bash
$ python main.py data/penguins.csv data/cleaned_penguins.csv
```

Processing an Excel file (remember to specify a `.csv` output file):
```bash 
$ python main.py data/titanic.xlsx data/cleaned_titanic.csv
```