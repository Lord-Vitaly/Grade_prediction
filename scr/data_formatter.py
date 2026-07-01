import pandas as pd
from . import data_loader as dl

def split_data(data: pd.DataFrame, test_perc: float, train_perc: float = None, valid_perc: float = None) -> None:
    '''
    Splits data to 3 sets: test, training (optional) and validation (optional) and saves to the corresponding files

    Args:
        data: pd.DataFrame that needs to be split
        test_perc: Percentage of the test set
        train_perc: Percentage of the training set (Optional)
        valid_perc: Percentage of the validation set (Optional)

    Return:
        None
    '''

    # Saving test set
    test_df = data.sample(frac=test_perc, random_state=42)
    dl.save(test_df, filename='test')

    data = data.drop(test_df.index)

    # Saving training set
    if train_perc is not None:
        train_df = data.sample(frac=train_perc, random_state=42)
    else:
        train_df = data
    dl.save(train_df, 'Training', 'training')

    if valid_perc is not None:
        # Saving validation set
        valid_df = data.drop(train_df.index)
        dl.save(valid_df, 'Validation', 'validation')


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