import pathlib as Path
from AuctionSummary.SQL.funcs import participating_cps, participating_crrahs
import crrdb.SQL._sql as sql
from AuctionSummary.Parse import funcs, crr_funcs
import streamlit as st
import pandas as pd
from automations.Auction_Summary.helpers import get_file_path, get_results_path
import time


def summarize(auction_name):
    start_time = time.time()

    # parse 'Auction Name' into paths in Go Live folder
    results_folder = get_results_path(auction_name)
    crr_file_path = get_file_path(auction_name)

    # query BidsOffersAndCRRs_After.csv file
    total_transactions_submitted = crr_funcs.get_total_transactions_submitted(
        crr_file_path)
    total_transactions_awarded = crr_funcs.get_total_transactions_awarded(
        crr_file_path)
    bid_mw = crr_funcs.get_bid_awarded_mw(crr_file_path)[0]
    awarded_mw = crr_funcs.get_bid_awarded_mw(crr_file_path)[1]
    obl_revenue = crr_funcs.get_obl_revenue(crr_file_path)
    opt_revenue = crr_funcs.get_opt_revenue(crr_file_path)
    new_capacity_bought = crr_funcs.get_awarded_mw_metrics(crr_file_path)[0]
    capacity_bought = crr_funcs.get_awarded_mw_metrics(crr_file_path)[1]
    volume_of_trade = crr_funcs.get_awarded_mw_metrics(crr_file_path)[2]

    # parse Convergence log
    last_iteration_num = funcs.parse_convergence_log(results_folder)[0]
    auction_duration = funcs.parse_convergence_log(results_folder)[1]

    # parse BindingConstraint.csv file
    total_binding_constraints = funcs.binding_constraint(results_folder)[0]
    non_budget_constraints = funcs.binding_constraint(results_folder)[1]
    unique_budget_constraints = funcs.binding_constraint(results_folder)[2]

    # parse WorstFlows.csv files in 'Worst Flows and Expanded Limits' folder
    # first_worst_flow = funcs.get_worst_flows(results_folder)[0]
    # second_worst_flow = funcs.get_worst_flows(results_folder)[1]
    # third_worst_flow = funcs.get_worst_flows(results_folder)[2]

    # query SQL
    crrahs = participating_crrahs(auction_name)
    cps_with_locked_credit = participating_cps(auction_name)[0]
    total_credit_locked = participating_cps(auction_name)[1]

    # Samantha requested
    opt_buy_bids_submitted = crr_funcs.get_buy_bids_submitted(crr_file_path)[0]
    obl_buy_bids_submitted = crr_funcs.get_buy_bids_submitted(crr_file_path)[1]
    opt_sell_bids_submitted = crr_funcs.get_sell_bids_submitted(crr_file_path)[
        0]
    obl_sell_bids_submitted = crr_funcs.get_sell_bids_submitted(crr_file_path)[
        1]
    opt_buy_bids_awarded = crr_funcs.get_buy_bids_awarded(crr_file_path)[0]
    obl_buy_bids_awarded = crr_funcs.get_buy_bids_awarded(crr_file_path)[1]
    opt_sell_bids_awarded = crr_funcs.get_sell_bids_awarded(crr_file_path)[0]
    obl_sell_bids_awarded = crr_funcs.get_sell_bids_awarded(crr_file_path)[1]

    # put results in DataFrame and display in app
    d = {"Metric": columns,
         "Value": [
             total_transactions_submitted,
             total_transactions_awarded,
             bid_mw,
             awarded_mw,
             obl_revenue,
             opt_revenue,
             new_capacity_bought,
             capacity_bought,
             volume_of_trade,
             last_iteration_num,
             auction_duration,
             total_binding_constraints,
             non_budget_constraints,
             unique_budget_constraints,
             #  first_worst_flow,
             #  second_worst_flow,
             #  third_worst_flow,
             opt_buy_bids_submitted,
             obl_buy_bids_submitted,
             opt_sell_bids_submitted,
             obl_sell_bids_submitted,
             opt_buy_bids_awarded,
             obl_buy_bids_awarded,
             opt_sell_bids_awarded,
             obl_sell_bids_awarded,
             crrahs,
             cps_with_locked_credit,
             total_credit_locked,
         ]}
    df = pd.DataFrame(data=d, dtype=str)
    st.dataframe(df, hide_index=True, height=600, width=350)
    function_time = time.time() - start_time
    return (st.markdown(f"Validation time: {round(function_time, 2)} seconds"),)


columns = [
    "Total Transactions Submitted",
    "Total Transactions Awarded",
    "Bid MW",
    "Awarded MW",
    "OBL Revenue",
    "OPT Revenue",
    "New Capacity Bought",
    "Capacity Bought",
    "Volume of Trade",
    "Num of Iterations",
    "Auction Duration",
    "Total Binding Constraints",
    "Non-Budget Constraints",
    "Unique Budget Constraints",
    # "PWD Worst Flow",
    # "OP Worst Flow",
    # "PWE Worst Flow",
    "OPT Buy Submitted",
    "OBL Buy Submitted",
    "OPT Sell Submitted",
    "OBL Sell Submitted",
    "OPT Buy Awarded",
    "OBL Buy Awarded",
    "OPT Sell Awarded",
    "OBL Sell Awarded",
    "Participating CRRAHs",
    "Total Locked Credit",
    "Participating CPs",
]


if __name__ == "__main__":
    summarize(r"2024.AUG.Monthly.Auction")
