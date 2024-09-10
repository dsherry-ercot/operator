from ercotdb import Database

crr = Database("pr07crr")


def get_cp_results(market_id):
    cp_query = f"""
    SELECT COUNT(DISTINCT smpc.ID_SMP) "CPs w/ Locked Credit",
        TO_CHAR(SUM(smpc.SMP_COLLATERAL), '$999,999,999,999.99') as "Total Credit Locked"
    FROM hedgeuser.FTR_MARKET mkt
    INNER JOIN hedgeuser.FTR_SMP_COLLATERAL smpc
        ON (mkt.ID = smpc.ID_MARKET)
    WHERE mkt.id = {market_id}
    AND smpc.SMP_COLLATERAL > 0
    """

    cp_results = crr.query(cp_query)

    total_credit_locked = cp_results.iloc[0, 1]
    CPs_with_locked_credit = cp_results.iloc[0, 0]
    return total_credit_locked, CPs_with_locked_credit


def get_CRRAH_results(market_id):
    crrah_query = f"""
    SELECT COUNT(DISTINCT port.id_mp) "CRRAHs w/ Submitted Bids",
       TO_CHAR(COUNT(bid.id), '999,999,999,999') "BidCount"
    FROM hedgeuser.FTR_MARKET mkt
    INNER JOIN hedgeuser.FTR_PORTFOLIO port
        ON (mkt.ID = port.ID_MARKET and port.credit_status = 4)
    INNER JOIN hedgeuser.FTR_PTP_BID bid
        ON (port.id = bid.id_portfolio)
    WHERE mkt.id = {market_id}
    """

    crrah_results = crr.query(crrah_query)

    bid_count = crrah_results.iloc[0, 1]
    CRRAHs_with_submitted_bids = crrah_results.iloc[0, 0]
    return CRRAHs_with_submitted_bids, bid_count


def get_recent_auctions():
    cp_query = f"""
    select name
    from HEDGEUSER.FTR_MARKET t
    order by id desc
    fetch first 10 rows only
    """

    cp_results = crr.query(cp_query)

    return cp_results


if __name__ == "__main__":

    print(get_cp_results())
    # my_query = f"""
    # select name
    # from HEDGEUSER.FTR_MARKET t
    # order by id desc
    # fetch first 10 rows only
    # """

    # results = crr.query(my_query)
    # print(results)
