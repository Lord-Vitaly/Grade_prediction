import pandas as pd
from pathlib import Path

def load(filename: str) -> pd.DataFrame:
    """Loads raw data from the data/raw directory.

    Args:
        file_name: Name of the file with extension (e.g., 'grades.csv').

    Returns:
        pd.DataFrame: Loaded dataset.
    """

    # 1. Get the absolute path of the current file (src/data_loader.py)
    current_file = Path(__file__).resolve()

    # 2. Go up to the project root and navigate to data/raw
    project_root = current_file.parent.parent
    file_path = project_root / "data" / "raw" / filename

    # 3. Check if the file exists before reading
    if not file_path.exists():
        raise FileNotFoundError(f"There is no file at: {file_path}")

    return pd.read_csv(file_path)

def save(dataframe: pd.DataFrame, filename: str = 'dataframe.csv') -> None:
    """Saves processed dataframe into file.

    Args:
        dataframe: Name of the dataframe;
        filename: Name of file with extension (default - dataframe.csv)

    Returns:
        None.
    """

    # 1. Get the path to the required directory
    current_file = Path(__file__).resolve()
    project_root = current_file.parent.parent
    file_path = project_root / 'data' / 'processed' / filename

    # 2. Save file
    dataframe.to_csv(fr'{file_path}', encoding='utf-8', index=False)