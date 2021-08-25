from typing import List

import pandas as pd

import schemas


def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_headers(df)
    df = validate_columns(df)
    df = dedupe_by_date(df)
    return df


def clean_headers(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = snake_case(list(df.columns))
    return df


def validate_columns(df: pd.DataFrame) -> pd.DataFrame:
    if not list(df.columns) == list(schemas.DFColumns.columns.keys()):
        raise ValueError("DF Columns do not adhere to the schema.")
    return df


def dedupe_by_date(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates(subset=["date"])


def snake_case(cols: List) -> List:
    return [x.lower().replace(" ", "_") for x in cols]
