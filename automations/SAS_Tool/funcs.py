from pathlib import Path
import polars as pl
from automations.SAS_Tool import bidsoffers_funcs as more_funcs
import automations.SAS_Tool.binding_funcs as binding_funcs
import streamlit as st


def ah_credit_exposure(
    results_folder,
):
    for file in Path(results_folder).iterdir():
        if "AHCreditExposure_After" in str(file) or "AHCreditExposure_Final" in str(
            file
        ):
            file_path = Path(results_folder, file)
            print(file_path)
            data = (
                pl.scan_csv(
                    str(file_path),
                    infer_schema_length=10000,
                    with_column_names=lambda cols: [col.strip() for col in cols],
                )
                .select(["Credit Worthy", "Total Exposure"])
                .filter(pl.col("Credit Worthy") == "No")
                .fill_null(0)
                .sum()
                .collect()
            )
            # print(data)
            sum_total_exposure = data["Total Exposure"][0]
            status = "PASS" if data["Total Exposure"][0] == 0 else "FAIL"

            return (
                st.markdown("**Credit Exposure**"),
                st.markdown(
                    f"{int(sum_total_exposure)} non-credit worthy CRRAHs with credit exposure -> {status}"
                ),
            )


def ah_eligibility(
    results_folder=r"Q:\CRR GoLive\Auction_Files\Monthly_Auctions\2024\2024_08_AUG\Results",
):
    for file in Path(results_folder).iterdir():
        if "AHEligibility" in str(file):
            file_path = Path(results_folder, file)
            print(file_path)
            data = (
                pl.scan_csv(
                    str(file_path),
                    infer_schema_length=10000,
                    with_column_names=lambda cols: [col.strip() for col in cols],
                )
                .select(
                    ["Account Holder Name", "Eligible Status", "Total Submitted Bids"]
                )
                .filter(pl.col("Eligible Status") == "No")
                .sum()
                .collect()
            )
            sum_submitted_bids = data["Total Submitted Bids"][0]
            status = "PASS" if data["Total Submitted Bids"][0] == 0 else "FAIL"
    return (
        st.markdown("**AH Eligibility**"),
        st.markdown(
            f"{sum_submitted_bids} submitted bids from ineligible CRRAHs -> {status}"
        ),
    )


def binding_constraint(
    results_folder=r"Q:\CRR GoLive\Auction_Files\Monthly_Auctions\2024\2024_08_AUG\Results",
):
    for file in Path(results_folder).iterdir():
        if "Binding" in str(file):
            file_path = Path(results_folder, file)
            print(file_path)
            binding_funcs.violation(file_path)
            binding_funcs.shadow_price(file_path)
            table = binding_funcs.high_shadow_prices(file_path)[1]
    return table


def bids_offers_crrs(
    results_folder=r"Q:\CRR GoLive\Auction_Files\Monthly_Auctions\2024\2024_08_AUG\Results",
):
    for file in Path(results_folder).iterdir():
        if "_After." in str(file):
            file_path = Path(results_folder, file)
            print(file_path)
            more_funcs.run_awarded_v_bid(file_path)
            more_funcs.run_buy_clear_v_bid(file_path)
            more_funcs.run_sell_clear_v_bid(file_path)
            more_funcs.run_OPT_sells(file_path)
            more_funcs.run_OPT_clearing(file_path)
            more_funcs.run_check_dates(file_path)
            more_funcs.run_OPT_buy_minimum(file_path)


def convergence_log(
    results_folder=r"Q:\CRR GoLive\Auction_Files\Monthly_Auctions\2024\2024_08_AUG\Results",
):
    for file in Path(results_folder).iterdir():
        if ".log" in str(file):
            file_path = Path(results_folder, file)
            print(file_path)
            counter = 0
            with open(file_path, "r") as doc:
                content_as_lst = doc.readlines()
                for line in content_as_lst:
                    if "OPF SOLUTION" in line:
                        counter += 1
                    if "ITERATIONS" in line:
                        iterations = line
                        continue
            status = "PASS" if counter > 0 else "FAIL"

    return (
        st.markdown("**Convergence Log**"),
        st.markdown(
            f"{counter} 'OPF SOLUTION IS COMPLETED' lines in Convergence Log -> {status}"
        ),
        status,
        iterations,
    )


if __name__ == "__main__":
    binding_constraint(
        # r"Q:\CRR GoLive\Auction_Files\Monthly_Auctions\2024\2024_08_AUG\Results\7832_BidsOffersAndCRRs_After.csv"
    )
