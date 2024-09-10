import pandas as pd
import os
import glob

monthly_file_path = r"C:\Users\dsherry\Desktop\2023 data files\Credit\Monthly"

ltas_file_path = r"C:\Users\dsherry\Desktop\2023 data files\Credit\LTAS Auctions"


def get_JAN_credit():

    AH = pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.JAN.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_FEB_Monthly_Crrs():
    return pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.FEB.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_MAR_Monthly_Crrs():
    return pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.MAR.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_APR_Monthly_Crrs():
    return pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.APR.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_MAY_Monthly_Crrs():
    return pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.MAY.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_JUN_Monthly_Crrs():
    return pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.JUN.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_JUL_Monthly_Crrs():
    return pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.JUL.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_AUG_Monthly_Crrs():
    return pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.AUG.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_SEP_Monthly_Crrs():
    return pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.SEP.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_OCT_Monthly_Crrs():
    return pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.OCT.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_NOV_Monthly_Crrs():
    return pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.NOV.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_DEC_Monthly_Crrs():
    return pd.read_csv(
        os.path.join(
            monthly_file_path, "2023.DEC.Monthly.Auction_BidsOffersAndCRRs_Posted.csv"
        )
    )
