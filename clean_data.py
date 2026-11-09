import pandas as pd
from get_data_types import categorical_cols, numeric_cols


def extract_file_type(filename: str) -> str:
    """Extract the file type from the filename extension"""

    file_type = filename.split('.')[-1]
    return file_type

def load_file(filename: str) -> pd.DataFrame:
    """Load a file based on its file type"""

    file_type = extract_file_type(filename)

    if file_type == 'csv':
        df = pd.read_csv(filename)
    elif file_type == 'json':
        df = pd.read_json(filename)
    elif file_type == 'xlsx':
        df = pd.read_excel(filename)
    elif file_type == 'parquet':    
        df = pd.read_parquet(filename)
    elif file_type == 'txt':            
        df = pd.read_csv(filename, delimiter='\t')
    elif file_type == 'tsv':
        df = pd.read_csv(filename, delimiter='\t')
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    return df


def clean_data(input_file: str, output_file: str) -> tuple[pd.DataFrame, list[str], list[str]]:
    """Clean the DataFrame by handling missing values and duplicates"""

    df = load_file(input_file)  # Load the data from the file

    # Drop duplicate rows
    df = df.drop_duplicates()
    
    # Fill missing numeric values with the median
    numeric_columns = numeric_cols(df)
    for col in numeric_columns:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)
    
    # Fill missing categorical values with the mode
    categorical_columns = categorical_cols(df)
    for col in categorical_columns:
        mode_value = df[col].mode()[0]
        df[col] = df[col].fillna(mode_value)

    # Export the cleaned DataFrame to csv file             
    df.to_csv(output_file, index=False)

    return df, numeric_columns, categorical_columns
