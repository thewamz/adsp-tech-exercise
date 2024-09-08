from pathlib import Path

import pandas as pd


def to_pandas(data):
    """Convert data into a pandas DataFrame"""
    return pd.json_normalize(data)


def to_csv(df, filename):
    """Store pandas DataFrame in csv file"""
    mode = "w"
    header = True

    if Path(filename).exists():
        mode = "a"
        header = False

    df.to_csv(filename, mode=mode, header=header)
