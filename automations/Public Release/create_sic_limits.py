import pandas as pd
import glob
import constants
import time

# import numpy


monthly_file_path = r"C:\Users\dsherry\Desktop\2023 data files\Credit\Monthly"

ltas_file_path = r"C:\Users\dsherry\Desktop\2023 data files\Credit\LTAS Auctions"

self_imposed_limits_path = (
    rf"{constants.YEAR} Self-Imposed Credit Limits - LTAS and Monthly Auctions.xlsx"
)


def ah_cp(value):
    if "X" in str(value):
        return "Account Holder"
    else:
        return "Counter Party"


# def digs(value):
#     # if len(str(value)) > 7:
#     return str(value).ljust(13, ".")
#     # return value


months = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC",
]

seqs = [
    "1st6.Seq1",
    "2nd6.Seq1",
    "1st6.Seq2",
    "2nd6.Seq2",
    "1st6.Seq3",
    "2nd6.Seq3",
    "1st6.Seq4",
    "2nd6.Seq4",
    "1st6.Seq5",
    "2nd6.Seq5",
    "1st6.Seq6",
    "2nd6.Seq6",
]


def get_credit_month(month):
    lst = []

    # monthly - create list of tuples from Account Holder workbooks
    address = glob.glob(f"{monthly_file_path}/*AH*{month}*")
    df = pd.read_csv(address[0])
    df = df.loc[df["Credit Limit"] >= 0, ["Account Holder", "Credit Limit"]]
    for _, row in df.iterrows():
        lst.append((row["Account Holder"], row["Credit Limit"]))

    # monthly - create list of tuples from Counter Party workbooks
    address = glob.glob(f"{monthly_file_path}/*arty*{month}*")
    df = pd.read_csv(address[0])
    df = df.loc[df["Credit Limit"] >= 0, ["Counter-Party", "Credit Limit"]]
    for _, row in df.iterrows():
        lst.append((row["Counter-Party"], row["Credit Limit"]))

    # create dataframe from two lists of tuples
    df = pd.DataFrame.from_records(
        lst, columns=["DUNS #/Short Name", "Self-Imposed Credit Limit"]
    )

    # adding "AH/CP" column based on if 'X' is in first column
    df["AH/CP"] = df["DUNS #/Short Name"].apply(ah_cp)
    # df["DUNS #/Short Name"] = df["DUNS #/Short Name"].apply(digs)
    # df.loc[:, "DUNS #/Short Name"] = df["DUNS #/Short Name"].map("{:13f}".format)

    # rearranging and returning df
    return df[["AH/CP", "DUNS #/Short Name", "Self-Imposed Credit Limit"]]


def get_credit_ltas(seq):
    lst = []

    # ltas - create list of tuples from Account Holder workbooks
    address = glob.glob(f"{ltas_file_path}/*AH*{seq}*")
    df = pd.read_csv(address[0])
    df = df.loc[
        df["Credit Limit"] >= 0, ["Account Holder", "Time Of Use", "Credit Limit"]
    ]
    for _, row in df.iterrows():
        lst.append((row["Account Holder"], row["Time Of Use"], row["Credit Limit"]))

    # ltas - create list of tuples from Counter Party workbooks
    address = glob.glob(f"{ltas_file_path}/*arty*{seq}*")
    df = pd.read_csv(address[0])
    df = df.loc[
        df["Credit Limit"] >= 0, ["Counter-Party", "Time Of Use", "Credit Limit"]
    ]
    for _, row in df.iterrows():
        lst.append((row["Counter-Party"], row["Time Of Use"], row["Credit Limit"]))

    # create dataframe from two lists of tuples
    df = pd.DataFrame.from_records(
        lst, columns=["DUNS #/Short Name", "Time Of Use", "Self-Imposed Credit Limit"]
    )

    # adding "AH/CP" column based on if 'X' is in first column
    df["AH/CP"] = df["DUNS #/Short Name"].apply(ah_cp)

    # rearranging and returning df
    return df[
        ["AH/CP", "DUNS #/Short Name", "Time Of Use", "Self-Imposed Credit Limit"]
    ]


def write_month():
    with pd.ExcelWriter(
        rf"C:\Users\dsherry\Desktop\{constants.YEAR} data files\{self_imposed_limits_path}",
    ) as wb:
        for month in months:
            df = get_credit_month(month)
            df.to_excel(
                wb,
                sheet_name=f"{month} {constants.YEAR}",
                index=False,
                float_format="%.2f",
            )


def write_ltas():
    with pd.ExcelWriter(
        rf"C:\Users\dsherry\Desktop\{constants.YEAR} data files\{self_imposed_limits_path}",
        mode="a",
        engine="openpyxl",
    ) as wb:
        for seq in seqs:
            df = get_credit_ltas(seq)
            df.to_excel(
                wb,
                sheet_name=f"{constants.YEAR}.{seq}",
                index=False,
                float_format="%.2f",
            )


if __name__ == "__main__":
    start_time = time.time()

    write_month()
    write_ltas()

    function_time = time.time() - start_time
    print(f"This took {function_time} seconds")
