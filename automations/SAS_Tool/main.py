import time
import automations.SAS_Tool.funcs as funcs
import streamlit as st
# from automations.SAS_Tool.send_email import send_email

from pathlib import Path


def get_files(auction_name):
    start_time = time.time()
    if "annual" in auction_name.lower():
        directory = Path(str("Q:\CRR GoLive\Auction_Files\LTAS_Auctions"))
        parent_folder = list(Path.glob(
            directory, rf"*\*{auction_name.replace('.', '_').replace('Auction', '')}*"))[0]
        results_folder = Path(parent_folder, "Results")
        credit_folder = Path(parent_folder, "Credit")
        print(f"{results_folder=}, {credit_folder=}")
    elif "month" in auction_name.lower():
        month_folder = get_month_folder_name(auction_name)
        directory = Path(str("Q:\CRR GoLive\Auction_Files\Monthly_Auctions"))
        year_folder = auction_name[:4]
        results_folder = Path(
            directory, year_folder, month_folder, "Results"
        )
        credit_folder = Path(
            directory, year_folder, month_folder, "Credit"
        )
        print(f"{results_folder=}, {credit_folder=}")
    print(f"Grabbing data from: {results_folder}")
    funcs.ah_eligibility(results_folder)
    table = funcs.binding_constraint(results_folder)
    funcs.ah_credit_exposure(credit_folder)
    convergence_status = funcs.convergence_log(
        results_folder)
    funcs.bids_offers_crrs(results_folder)

    # send_email(
    #     auction_name,
    #     results_folder,
    #     convergence_status[2],
    #     convergence_status[3]
    #     .strip()
    #     .split()[
    #         -1
    #     ],
    #     table,
    # )
    # except Exception as e:
    #     print(f"{month_folder} threw an exception")
    #     print(e)
    #     continue

    function_time = time.time() - start_time
    return (st.markdown(f"Validation time: {round(function_time, 2)} seconds"),)


month_dict = {
    "JAN": "01",
    "FEB": "02",
    "MAR": "03",
    "APR": "04",
    "MAY": "05",
    "JUN": "06",
    "JUL": "07",
    "AUG": "08",
    "SEP": "09",
    "OCT": "10",
    "NOV": "11",
    "DEC": "12",
}


def get_month_folder_name(auction: str = "2024.AUG.Monthly.Auction") -> str:
    """
    Turns "2024.AUG.Monthly.Auction" into "2024_08_AUG"
    """
    year = auction[:4]
    month = auction[5:8]
    month_number = month_dict[month]
    return f"{year}_{month_number}_{month}"


if __name__ == "__main__":
    get_files("2026.2nd6.AnnualAuction.Seq5")
    get_files("2024.SEP.Monthly.Auction")
