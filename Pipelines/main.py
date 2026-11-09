from clean_data import clean_data
from visualize import categorical_distributions_plot, scatter_splom


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Input file for cleaning and visualizing (formats accepted: CSV, JSON, Excel, Parquet, TXT, TSV)")
    parser.add_argument("output_file", help="Path and filename where cleaned data will be exported (e.g., data/cleaned_penguins.csv)")

    args = parser.parse_args()
    
    # Clean the data filling in missing values (median for numeric, mode for categorical) and removing duplicates
    df_cleaned, numeric_columns, categorical_columns = clean_data(args.input_file, args.output_file)
    
    # Visualize the data - scatter matrix for numeric columns and count distributions for categorical columns
    scatter_splom(df_cleaned[numeric_columns]) 
    categorical_distributions_plot(df_cleaned[categorical_columns]) 
