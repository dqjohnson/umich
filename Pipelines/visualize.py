import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from get_data_types import numeric_cols, categorical_cols

def scatter_splom(df: pd.DataFrame, alpha: float = 0.8, figsize: tuple = (8, 8), title: str = 'Scatter Matrix of Numeric Columns') -> None:
    """Create a scatter matrix for the DataFrame for numerical columns"""
    numeric_columns = numeric_cols(df)
    pd.plotting.scatter_matrix(df[numeric_columns], alpha=alpha, figsize=figsize, diagonal='hist')
    fig = plt.gcf()
    fig.suptitle(title)
    plt.tight_layout()
    plt.show()

def categorical_distributions_plot(
    df: pd.DataFrame, col_width: float = 4.5, fig_height: float = 4.5, palette: str = "pastel", ylabel: str = "Count",
    title: str = "Categorical Distributions", num_rows: int = 1) -> None:
    """Plot count distributions for all categorical columns side-by-side."""

    cat_cols = categorical_cols(df)
    if not cat_cols:
        return

    num_cols = len(cat_cols)
    fig, axes = plt.subplots(
        nrows=num_rows, ncols=num_cols, figsize=(col_width * num_cols, fig_height), squeeze=False, sharey=True
    )

    for i, col in enumerate(cat_cols):
        sns.countplot(data=df, x=col, hue=col, ax=axes[0, i], palette=palette, legend=False)
        axes[0, i].set_title(f"Distribution of {col}")
        axes[0, i].set_xlabel(col)
        if i == 0:
            axes[0, i].set_ylabel(ylabel)
        else:
            axes[0, i].set_ylabel("")

    fig = plt.gcf()
    fig.suptitle(title)

    plt.tight_layout()
    plt.show()
