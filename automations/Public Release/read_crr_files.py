import pandas as pd
import os

monthly_file_path = (
    r"C:\Users\dsherry\Desktop\2023 data files\PTP Bids and CRRs\Monthly"
)

ltas_file_path = (
    r"C:\Users\dsherry\Desktop\2023 data files\PTP Bids and CRRs\LTAS Auctions"
)


def get_JAN_Monthly_Crrs():
    return pd.read_csv(
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


# Seq1 & Seq2
def get_seq1_1st6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.1st6.Annual.Seq1_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_seq1_2nd6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.2nd6.Annual.Seq1_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_seq2_1st6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.1st6.Annual.Seq2_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_seq2_2nd6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.2nd6.Annual.Seq2_BidsOffersAndCRRs_Posted.csv"
        )
    )


# Seq3 & Seq4
def get_seq3_1st6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.1st6.Annual.Seq3_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_seq3_2nd6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.2nd6.Annual.Seq3_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_seq4_1st6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.1st6.Annual.Seq4_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_seq4_2nd6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.2nd6.Annual.Seq4_BidsOffersAndCRRs_Posted.csv"
        )
    )


# Seq5 & Seq6
def get_seq5_1st6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.1st6.Annual.Seq5_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_seq5_2nd6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.2nd6.Annual.Seq5_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_seq6_1st6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.1st6.Annual.Seq6_BidsOffersAndCRRs_Posted.csv"
        )
    )


def get_seq6_2nd6_LTAS_Crrs():
    return pd.read_csv(
        os.path.join(
            ltas_file_path, "2023.2nd6.Annual.Seq6_BidsOffersAndCRRs_Posted.csv"
        )
    )
