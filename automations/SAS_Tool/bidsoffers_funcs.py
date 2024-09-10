import polars as pl
from . import st


def run_awarded_v_bid(file_path):
    awarded_vs_bid = (
        pl.scan_csv(
            str(file_path),
            infer_schema_length=10000,
            with_column_names=lambda cols: [col.strip().lower() for col in cols],
        )
        .select(["awarded mw", "bid mw"])
        .filter(pl.col("awarded mw") > pl.col("bid mw"))
        .count()
        .collect()
    )

    awardedMW_gt_bidMW = awarded_vs_bid[0, 1]
    status = "PASS" if awardedMW_gt_bidMW == 0 else "FAIL"

    return (
        st.markdown("**Bids Offers and CRRs**"),
        st.markdown(
            f"1. {awardedMW_gt_bidMW} rows with Awarded MW > Bid MW -> {status}"
        ),
    )


def run_buy_clear_v_bid(file_path):
    buy_clear_vs_bid = (
        pl.scan_csv(
            str(file_path),
            infer_schema_length=10000,
            with_column_names=lambda cols: [col.strip().lower() for col in cols],
        )
        .select(["class", "awarded mw", "bid price", "clearing price"])
        .filter(
            (pl.col("awarded mw") > 0)
            & (pl.col("clearing price") > pl.col("bid price"))
            & (pl.col("class") == "BUY")
        )
        .count()
        .collect()
    )

    buy_check = buy_clear_vs_bid[0, 3]
    status = "PASS" if buy_check == 0 else "FAIL"

    return st.markdown(
        f"2. {buy_check} awarded BUYs with 'Clearing Price' > 'Bid Price' -> {status}"
    )


def run_sell_clear_v_bid(file_path):
    sell_clear_vs_bid = (
        pl.scan_csv(
            str(file_path),
            infer_schema_length=10000,
            with_column_names=lambda cols: [col.strip().lower() for col in cols],
        )
        .select(["class", "awarded mw", "bid price", "clearing price"])
        .filter(
            (pl.col("awarded mw") > 0)
            & (pl.col("clearing price") < pl.col("bid price"))
            & (pl.col("class") == "SELL")
        )
        .count()
        .collect()
    )

    sell_check = sell_clear_vs_bid[0, 3]
    status = "PASS" if sell_check == 0 else "FAIL"

    return st.markdown(
        f"3. {sell_check} awarded SELLs with 'Clearing Price' < 'Bid Price' -> {status}"
    )


def run_OPT_sells(file_path):
    neg_OPT_sells = (
        pl.scan_csv(
            str(file_path),
            infer_schema_length=10000,
            with_column_names=lambda cols: [col.strip().lower() for col in cols],
        )
        .select(
            [
                "class",
                "awarded mw",
                "bid mw",
                "bid price",
                "hedge type",
                "credit consumed per mw",
            ]
        )
        .filter(
            (pl.col("hedge type") == "OPT")
            & (pl.col("class") == "SELL")
            & (pl.col("awarded mw") != pl.col("bid mw"))
            & (pl.col("bid price") < 0)
        )
        .count()
        .collect()
    )

    neg_OPT = neg_OPT_sells[0, 3]
    status = "PASS" if neg_OPT == 0 else "FAIL"

    return st.markdown(
        f"{neg_OPT} negatively priced OPT Sells not fully awarded -> {status}"
    )


def run_OPT_clearing(file_path):
    opt_clearing = (
        pl.scan_csv(
            str(file_path),
            infer_schema_length=10000,
            with_column_names=lambda cols: [col.strip().lower() for col in cols],
        )
        .select(
            [
                "hedge type",
                "clearing price",
            ]
        )
        .filter((pl.col("hedge type") == "OPT") & (pl.col("clearing price") < 0))
        .count()
        .collect()
    )

    neg_OPT = opt_clearing[0, 1]
    status = "PASS" if neg_OPT == 0 else "FAIL"

    return st.markdown(
        f"5. {neg_OPT} negative clearing prices for OPT bids -> {status}"
    )


def run_check_dates(file_path):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    check_dates = (
        pl.scan_csv(
            str(file_path),
            infer_schema_length=10000,
            with_column_names=lambda cols: [col.strip().lower() for col in cols],
        )
        .select(
            [
                "awarded mw",
                "start date",
                "end date",
            ]
        )
        .filter((pl.col("awarded mw") > 0))
        .unique(subset=["start date", "end date"])
        .collect()
    )

    start_date = datetime.strptime(check_dates[0, 1], "%m/%d/%Y").date()
    end_of_month = start_date + relativedelta(day=31)
    end_date = datetime.strptime(check_dates[0, 2], "%m/%d/%Y").date()

    status = (
        "PASS"
        if start_date.day == 1 and end_date == end_of_month and start_date < end_date
        else "FAIL"
    )

    return st.markdown(
        f"10. Start date < End date and start/end date are beggining/end of month -> {status}"
    )


def run_OPT_buy_minimum(file_path):
    opt_clearing = (
        pl.scan_csv(
            str(file_path),
            infer_schema_length=10000,
            with_column_names=lambda cols: [col.strip().lower() for col in cols],
        )
        .select(["hedge type", "class", "bid price"])
        .filter(
            (pl.col("hedge type") == "OPT")
            & (pl.col("class") == "BUY")
            & pl.col("bid price").lt(0.01)
        )
        .count()
        .collect()
    )

    min_bid_price = opt_clearing[0, 1]
    status = "PASS" if min_bid_price == 0 else "FAIL"

    return st.markdown(
        f"18. {min_bid_price} OPT BUYS with 'Bid Price' < $.01 -> {status}"
    )


# f"11. {neg_OPT} negative clearing prices for OPT bids -> {status}"

if __name__ == "__main__":
    run_OPT_buy_minimum(
        r"Q:\CRR GoLive\Auction_Files\Monthly_Auctions\2024\2024_08_AUG\Results\7832_BidsOffersAndCRRs_After.csv"
    )
