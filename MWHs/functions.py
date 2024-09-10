import os
from pathlib import Path
import pandas as pd
import polars as pl


def build_df_month(results_folder, month_folder):

    for file in Path(results_folder).iterdir():
        if "fter." in str(file) and "xlsx" not in str(file) and "CRR" in str(file):
            file_path = Path(results_folder, file)
            data = (
                pl.scan_csv(
                    str(file_path),
                    infer_schema_length=10000,
                    with_column_names=lambda cols: [col.strip() for col in cols],
                )
            ).collect()

            data = data.with_columns(
                (pl.col("Awarded Mw") * pl.col("Number Of Hours")).alias(
                    "Awarded MWHs"
                ),
                (pl.col("Bid MW") * pl.col("Number Of Hours")).alias("Bid MWHs"),
                (
                    pl.col("Awarded Mw")
                    * pl.col("Number Of Hours")
                    * pl.col("Clearing Price")
                ).alias("Awarded MWHs Clearing Price"),
                (
                    pl.col("Bid Price") * pl.col("Bid MW") * pl.col("Number Of Hours")
                ).alias("Bid MWHs Bid Price"),
            )

            # Pivot table
            data = data.group_by(["Start Date", "Class", "Hedge Type"]).agg(
                pl.col("Number Of Hours").sum(),
                pl.col("Bid MW").sum(),
                pl.col("Bid Price").sum(),
                pl.col("Bid MWHs").sum(),
                pl.col("Bid MWHs Bid Price").sum(),
                pl.col("Awarded Mw").sum(),
                pl.col("Clearing Price").sum(),
                pl.col("Awarded MWHs").sum(),
                pl.col("Awarded MWHs Clearing Price").sum(),
            )

            auction_name = parse_month_auction_name(month_folder)

            # adding two weighted calculations
            data = data.with_columns(
                (pl.col("Awarded MWHs Clearing Price") / pl.col("Awarded MWHs")).alias(
                    "Weighted Avg Clear Price"
                ),
                (pl.col("Bid MWHs Bid Price") / pl.col("Bid MWHs")).alias(
                    "Weighted Avg Bid Price"
                ),
                (pl.lit(auction_name).alias("Auction")),
                (pl.lit(str(file).split("\\")[-1][:4])).alias("Market ID"),
            )

            df = data.to_pandas().round(2)

            # # write to csv. If first entry then include headers
            if not os.path.isfile(f"{os.getcwd()}/MWHs/data_month.csv"):
                write_csv_headers(df)
            else:
                write_csv_no_headers(df)


def build_df_ltas(results_folder, ltas_auction):
    for file in Path(results_folder).iterdir():
        if "fter." in str(file) and "xlsx" not in str(file) and "CRR" in str(file):
            file_path = Path(results_folder, file)
            data = (
                pl.scan_csv(
                    str(file_path),
                    infer_schema_length=10000,
                    with_column_names=lambda cols: [col.strip() for col in cols],
                )
            ).collect()

            data = data.with_columns(
                (pl.col("Awarded Mw") * pl.col("Number Of Hours")).alias(
                    "Awarded MWHs"
                ),
                (pl.col("Bid MW") * pl.col("Number Of Hours")).alias("Bid MWHs"),
                (
                    pl.col("Awarded Mw")
                    * pl.col("Number Of Hours")
                    * pl.col("Clearing Price")
                ).alias("Awarded MWHs Clearing Price"),
                (
                    pl.col("Bid Price") * pl.col("Bid MW") * pl.col("Number Of Hours")
                ).alias("Bid MWHs Bid Price"),
            )

            # Pivot table
            data = data.group_by(
                ["Start Date", "Class", "Hedge Type", "Time Of Use"]
            ).agg(
                pl.col("Number Of Hours").sum(),
                pl.col("Bid MW").sum(),
                pl.col("Bid Price").sum(),
                pl.col("Bid MWHs").sum(),
                pl.col("Bid MWHs Bid Price").sum(),
                pl.col("Awarded Mw").sum(),
                pl.col("Clearing Price").sum(),
                pl.col("Awarded MWHs").sum(),
                pl.col("Awarded MWHs Clearing Price").sum(),
            )

            auction_name = parse_ltas_auction_name(results_folder)

            # adding two weighted calculations
            data = data.with_columns(
                (pl.col("Awarded MWHs Clearing Price") / pl.col("Awarded MWHs")).alias(
                    "Weighted Avg Clear Price"
                ),
                (pl.col("Bid MWHs Bid Price") / pl.col("Bid MWHs")).alias(
                    "Weighted Avg Bid Price"
                ),
                (pl.lit(auction_name).alias("Auction")),
                (pl.lit(str(file).split("\\")[-1][:4])).alias("Market ID"),
            )

            df = data.to_pandas().round(2)

            # write to csv. If first entry then include headers
            if not os.path.isfile(f"{os.getcwd()}/MWHs/data_ltas.csv"):
                write_csv_headers_ltas(df)
            else:
                write_csv_no_headers_ltas(df)


def parse_month_auction_name(month_folder):
    month_folder = str(month_folder).split("\\")[-1]
    year = month_folder[:4]
    month = month_folder[-3:]
    return f"{year}.{month}.Monthly.Auction"


def parse_ltas_auction_name(results_folder):
    results_folder = str(results_folder).split("\\")[-2]
    year = results_folder[4:8]
    seq = results_folder[-4:]
    term = results_folder[9:13]
    return f"{year}.{term}.AnnualAuction.{seq}"


def write_csv_headers(df):
    df.to_csv(f"{os.getcwd()}/MWHs/data_month.csv", mode="a", header=True, index=False)


def write_csv_no_headers(df):
    df.to_csv(f"{os.getcwd()}/MWHs/data_month.csv", mode="a", header=False, index=False)


def write_csv_headers_ltas(df):
    df.to_csv(f"{os.getcwd()}/MWHs/data_ltas.csv", mode="a", header=True, index=False)


def write_csv_no_headers_ltas(df):
    df.to_csv(f"{os.getcwd()}/MWHs/data_ltas.csv", mode="a", header=False, index=False)


# def build_df_ltas(results_folder, ltas_auction):
#     for file in Path(results_folder).iterdir():
#         if "fter." in str(file):
#             file_path = Path(results_folder, file)
#             data = pd.read_csv(
#                 str(file_path), encoding="unicode_escape", skipinitialspace=True
#             )
#             # Adding columns
#             data["Awarded MWHs"] = data["Awarded Mw"] * data["Number Of Hours"]
#             data["Bid MWHs"] = data["Bid MW"] * data["Number Of Hours"]

#             # Calculated Columns
#             data["Awarded MWHs Clearing Price"] = (
#                 data["Awarded MWHs"] * data["Clearing Price"]
#             )
#             data["Bid MWHs Bid Price"] = data["Bid MWHs"] * data["Bid Price"]
#             # Pivot table
#             df = (
#                 data.groupby(["Start Date", "Class", "Hedge Type", "Time Of Use"])[
#                     [
#                         "Number Of Hours",
#                         "Bid MW",
#                         "Bid Price",
#                         "Bid MWHs",
#                         "Bid MWHs Bid Price",
#                         "Awarded Mw",
#                         "Clearing Price",
#                         "Awarded MWHs",
#                         "Awarded MWHs Clearing Price",
#                     ]
#                 ]
#             ).sum()

#             # adding two weighted calculations
#             df["Weighted Avg Bid Price"] = (
#                 df["Awarded MWHs Clearing Price"] / df["Awarded MWHs"]
#             )
#             df["Weighted Avg Clear Price"] = df["Bid MWHs Bid Price"] / df["Bid MWHs"]
#             df["Auction"] = (
#                 str(ltas_auction)
#                 .split("\\")[-1][4:]
#                 .replace("_", ".")
#                 .replace("Annual", "AnnualAuction")
#             )

#             # write to csv. If first entry then include headers
#             if not os.path.isfile(f"{os.getcwd()}/MWHs/data_ltas_test.csv"):
#                 write_csv_headers_ltas(df)
#             else:
#                 write_csv_no_headers_ltas(df)


# def build_df_month(results_folder, month_folder):
#     for file in Path(results_folder).iterdir():
#         if "fter" in str(file):
#             file_path = Path(results_folder, file)
#             data = pd.read_csv(
#                 str(file_path),
#                 encoding="unicode_escape",
#                 header=0,
#                 names=[
#                     "Bid ID",
#                     "CRR ID",
#                     "Ori CRR ID",
#                     "Portfolio",
#                     "Account Holder",
#                     "Source",
#                     "Sink",
#                     "Hedge Type",
#                     "Class",
#                     "Type",
#                     "Time Of Use",
#                     "24 Hour Bid",
#                     "Start Date",
#                     "End Date",
#                     "Bid MW",
#                     "Bid Price",
#                     "Awarded Mw",
#                     "Clearing Price",
#                     "Transaction Amount",
#                     "Credit Consumed Per Mw	",
#                     "Number Of Hours",
#                 ],
#             )
#             # Adding columns
#             data["Awarded MWHs"] = data["Awarded Mw"] * data["Number Of Hours"]
#             data["Bid MWHs"] = data["Bid MW"] * data["Number Of Hours"]

#             # Calculated Columns
#             data["Awarded MWHs Clearing Price"] = (
#                 data["Awarded MWHs"] * data["Clearing Price"]
#             )
#             data["Bid MWHs Bid Price"] = data["Bid MWHs"] * data["Bid Price"]

#             # Pivot table
#             df = (
#                 data.groupby(
#                     ["Start Date", "Class", "Hedge Type"]
#                 )[  # for LTAS group by TOU as well
#                     [
#                         "Number Of Hours",
#                         "Bid MW",
#                         "Bid Price",
#                         "Bid MWHs",
#                         "Bid MWHs Bid Price",
#                         "Awarded Mw",
#                         "Clearing Price",
#                         "Awarded MWHs",
#                         "Awarded MWHs Clearing Price",
#                     ]
#                 ]
#             ).sum()

#             # adding two weighted calculations
#             df["Weighted Avg Bid Price"] = (
#                 df["Awarded MWHs Clearing Price"] / df["Awarded MWHs"]
#             )
#             df["Weighted Avg Clear Price"] = df["Bid MWHs Bid Price"] / df["Bid MWHs"]
#             df["Auction"] = str(month_folder).split("\\")[-1]

#             # write to csv. If first entry then include headers
#             if not os.path.isfile(f"{os.getcwd()}/MWHs/data_month.csv"):
#                 write_csv_headers(df)
#             else:
#                 write_csv_no_headers(df)
