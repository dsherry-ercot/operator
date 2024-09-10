import os
from constants import parent, credit, bidsCRRs, ltas, monthly


def get_file_suffix_monthly(folder):
    year = folder[:4]
    month = folder[-3:]
    return f"_{month}_{year}.csv"


def get_file_prefix_monthly(folder):
    year = folder[:4]
    month = folder[-3:]
    return f"{year}.{month}.Monthly.Auction"


def get_file_suffix_ltas(folder):
    year = folder[4:8]
    term = folder[9:13]
    sequence = folder[-4:]
    return f"_{year}.{term}.{sequence}.csv"


def get_file_prefix_ltas(folder):
    year = folder[4:8]
    term = folder[9:13]
    sequence = folder[-4:]
    return f"{year}.{term}.Annual.{sequence}"


# Step 2: creating folder structure
def make_folders():
    if not os.path.exists(parent):
        os.mkdir(parent)
        os.mkdir(credit)
        os.mkdir(bidsCRRs)
        os.mkdir(rf"{credit}\{ltas}")
        os.mkdir(rf"{credit}\{monthly}")
        os.mkdir(rf"{bidsCRRs}\{ltas}")
        os.mkdir(rf"{bidsCRRs}\{monthly}")
