import pandas as pd

def numeric_cols(df: pd.DataFrame) -> list:
    """Return a list of numeric columns from the DataFrame"""
    return df.select_dtypes(include=["number"]).columns.tolist()

def categorical_cols(df: pd.DataFrame) -> list:
    """Return a list of categorical columns from the DataFrame"""
    return df.select_dtypes(include=["object", "category"]).columns.tolist()
