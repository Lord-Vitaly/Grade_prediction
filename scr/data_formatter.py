import pandas as pd
import data_loader as dl

def format_data(filename: str) -> pd.DataFrame:
    '''
    Formats data in csv-file and converts it to pd.Dataframe

    Args:
        filename: Name of the csv-file.

    Return:
        Formated pd.Dataframe.
    '''

    # 1. Loading file.
    df = dl.load(filename)

    # 2. Converting binary and categorical features to numeral.
    for col in df.columns:
        if df[col].nunique() == 2:                          # If it is binary...
            df[col] = df[col].astype('category').cat.codes  # Converts to categoical -> numeral

    df = pd.get_dummies(df, drop_first=True, dtype=int)     # Converts categorical to binary

    return df