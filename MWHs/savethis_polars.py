import os
import polars as pl
from pathlib import Path
import pandas as pd


def build_df(results_folder, month_folder):
    for file in Path(results_folder).iterdir():
        if "ted" in str(file):
            file_path = Path(results_folder, file)
            print(file_path)
            data = (
                pl.scan_csv(str(file_path))
                .group_by(" Start Date", " Class", " Hedge Type")
                .agg(
                    pl.col(
                        " Number Of Hours",
                        " Bid MW",
                        " Awarded Mw",
                        " Clearing Price",
                    ).sum()
                )
                .with_columns(pl.lit(month_folder).alias("Auction"))
            )

            df = data.collect()
            df.head(5)
            df = df.to_pandas()
            print(df.head(5))

            if not os.path.isfile(f"{os.getcwd()}/MWHs/2024_data.csv"):
                write_csv_headers(df)
            else:
                write_csv_no_headers(df)


def write_csv_headers(df):
    df.to_csv(
        f"{os.getcwd()}/MWHs/2024_data.csv",
        mode="a",
        header=True,
    )


def write_csv_no_headers(df):
    df.to_csv(
        f"{os.getcwd()}/MWHs/2024_data.csv",
        mode="a",
        header=False,
    )
