import polars as pl
import pandas as pd
import constants
import os
import read_crr_files


credit_workbook = (
    "2023 Self-Imposed Credit Limits - LTAS and Monthly Auctions_test.xlsx"
)
JanJunMonthly_BidsCrrs = f"{constants.parent}\{constants.YEAR} PTP Bids and CRRs - JAN-JUN Monthly Auctions_test.xlsx"

JulDecMonthly_BidsCrrs = f"{constants.parent}\{constants.YEAR} PTP Bids and CRRs - JUL-DEC Monthly Auctions_test.xlsx"

Seq1_Seq2_BidsCrrs = (
    f"{constants.parent}\{constants.YEAR} PTP Bids and CRRs - LTAS Seq1-2 Auctions.xlsx"
)

Seq3_Seq4_BidsCrrs = (
    f"{constants.parent}\{constants.YEAR} PTP Bids and CRRs - LTAS Seq3-4 Auctions.xlsx"
)

Seq5_Seq6_BidsCrrs = (
    f"{constants.parent}\{constants.YEAR} PTP Bids and CRRs - LTAS Seq5-6 Auctions.xlsx"
)

self_imposed_credit_limits = (
    f"{constants.YEAR} Self-Imposed Credit Limits - LTAS and Monthly Auctions.xlsx"
)


def drop_portfolio_column(filepath):
    return pl.read_csv(
        filepath,
        infer_schema_length=10000,
    ).drop([" Portfolio", "Portfolio"])


def write_janjun_monthly_BidsCrrs():
    if not os.path.exists(JanJunMonthly_BidsCrrs):

        with pd.ExcelWriter(JanJunMonthly_BidsCrrs) as wb:
            df_JAN = read_crr_files.get_JAN_Monthly_Crrs()
            df_FEB = read_crr_files.get_FEB_Monthly_Crrs()
            df_MAR = read_crr_files.get_MAR_Monthly_Crrs()
            df_APR = read_crr_files.get_APR_Monthly_Crrs()
            df_MAY = read_crr_files.get_MAY_Monthly_Crrs()
            df_JUN = read_crr_files.get_JUN_Monthly_Crrs()

            df_JAN.to_excel(
                wb, sheet_name=f"JAN_{constants.YEAR}_Monthly_Auction", index=False
            )
            df_FEB.to_excel(
                wb, sheet_name=f"FEB_{constants.YEAR}_Monthly_Auction", index=False
            )
            df_MAR.to_excel(
                wb, sheet_name=f"MAR_{constants.YEAR}_Monthly_Auction", index=False
            )
            df_APR.to_excel(
                wb, sheet_name=f"APR_{constants.YEAR}_Monthly_Auction", index=False
            )
            df_MAY.to_excel(
                wb, sheet_name=f"MAY_{constants.YEAR}_Monthly_Auction", index=False
            )
            df_JUN.to_excel(
                wb, sheet_name=f"JUN_{constants.YEAR}_Monthly_Auction", index=False
            )


def write_juldec_monthly_BidsCrrs():
    if not os.path.exists(JulDecMonthly_BidsCrrs):

        with pd.ExcelWriter(JulDecMonthly_BidsCrrs) as wb:
            df_JUL = read_crr_files.get_JUL_Monthly_Crrs()
            df_AUG = read_crr_files.get_AUG_Monthly_Crrs()
            df_SEP = read_crr_files.get_SEP_Monthly_Crrs()
            df_OCT = read_crr_files.get_OCT_Monthly_Crrs()
            df_NOV = read_crr_files.get_NOV_Monthly_Crrs()
            df_DEC = read_crr_files.get_DEC_Monthly_Crrs()

            df_JUL.to_excel(
                wb, sheet_name=f"JUL_{constants.YEAR}_Monthly_Auction", index=False
            )
            df_AUG.to_excel(
                wb, sheet_name=f"AUG_{constants.YEAR}_Monthly_Auction", index=False
            )
            df_SEP.to_excel(
                wb, sheet_name=f"SEP_{constants.YEAR}_Monthly_Auction", index=False
            )
            df_OCT.to_excel(
                wb, sheet_name=f"OCT_{constants.YEAR}_Monthly_Auction", index=False
            )
            df_NOV.to_excel(
                wb, sheet_name=f"NOV_{constants.YEAR}_Monthly_Auction", index=False
            )
            df_DEC.to_excel(
                wb, sheet_name=f"DEC_{constants.YEAR}_Monthly_Auction", index=False
            )


def write_seq1_seq2():
    if not os.path.exists(Seq1_Seq2_BidsCrrs):

        with pd.ExcelWriter(Seq1_Seq2_BidsCrrs) as wb:
            df_seq1_1st6 = read_crr_files.get_seq1_1st6_LTAS_Crrs()
            df_seq1_2nd6 = read_crr_files.get_seq1_2nd6_LTAS_Crrs()
            df_seq2_1st6 = read_crr_files.get_seq2_1st6_LTAS_Crrs()
            df_seq2_2nd6 = read_crr_files.get_seq2_2nd6_LTAS_Crrs()

            df_seq1_1st6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.1st6.Seq1", index=False
            )
            df_seq1_2nd6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.2nd6.Seq1", index=False
            )
            df_seq2_1st6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.1st6.Seq2", index=False
            )
            df_seq2_2nd6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.2nd6.Seq2", index=False
            )


def write_seq3_seq4():
    if not os.path.exists(Seq3_Seq4_BidsCrrs):

        with pd.ExcelWriter(Seq3_Seq4_BidsCrrs) as wb:
            df_seq3_1st6 = read_crr_files.get_seq3_1st6_LTAS_Crrs()
            df_seq3_2nd6 = read_crr_files.get_seq3_2nd6_LTAS_Crrs()
            df_seq4_1st6 = read_crr_files.get_seq4_1st6_LTAS_Crrs()
            df_seq4_2nd6 = read_crr_files.get_seq4_2nd6_LTAS_Crrs()

            df_seq3_1st6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.1st6.Seq3", index=False
            )
            df_seq3_2nd6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.2nd6.Seq3", index=False
            )
            df_seq4_1st6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.1st6.Seq4", index=False
            )
            df_seq4_2nd6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.2nd6.Seq4", index=False
            )


def write_seq5_seq6():
    if not os.path.exists(Seq5_Seq6_BidsCrrs):

        with pd.ExcelWriter(Seq5_Seq6_BidsCrrs) as wb:
            df_seq5_1st6 = read_crr_files.get_seq5_1st6_LTAS_Crrs()
            df_seq5_2nd6 = read_crr_files.get_seq5_2nd6_LTAS_Crrs()
            df_seq6_1st6 = read_crr_files.get_seq6_1st6_LTAS_Crrs()
            df_seq6_2nd6 = read_crr_files.get_seq6_2nd6_LTAS_Crrs()

            df_seq5_1st6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.1st6.Seq5", index=False
            )
            df_seq5_2nd6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.2nd6.Seq5", index=False
            )
            df_seq6_1st6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.1st6.Seq6", index=False
            )
            df_seq6_2nd6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.2nd6.Seq6", index=False
            )


def write_si_credit_limits():
    if not os.path.exists(self_imposed_credit_limits):

        with pd.ExcelWriter(self_imposed_credit_limits) as wb:
            df_seq5_1st6 = read_crr_files.get_seq5_1st6_LTAS_Crrs()
            df_seq5_2nd6 = read_crr_files.get_seq5_2nd6_LTAS_Crrs()
            df_seq6_1st6 = read_crr_files.get_seq6_1st6_LTAS_Crrs()
            df_seq6_2nd6 = read_crr_files.get_seq6_2nd6_LTAS_Crrs()

            df_seq5_1st6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.1st6.Seq5", index=False
            )
            df_seq5_2nd6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.2nd6.Seq5", index=False
            )
            df_seq6_1st6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.1st6.Seq6", index=False
            )
            df_seq6_2nd6.to_excel(
                wb, sheet_name=f"{constants.YEAR}.2nd6.Seq6", index=False
            )
