from ercotdb import Database
from components.SQLqueries import get_marketid
import streamlit as st

prod = Database(dbname="PR07CRR")


@st.cache_data
def run_analysis_query():
    # market_id = get_marketid.get_market_id(auction_name)

    df = prod.query(
        f"""
    with CPs as
 (select mkt.id,
         mkt.name,
         count(distinct smpc.ID_SMP) as participating_CPs,
         to_char(sum(smpc.smp_collateral), '$999,999,999,999.99') as final_locked_credit
    from hedgeuser.ftr_market mkt
   inner join hedgeuser.ftr_smp_collateral smpc
      on (mkt.id = smpc.id_market)
   where smpc.smp_collateral > 0
     and mkt.id >= 7000
   group by mkt.id, mkt.name),

CRRAHs as
 (SELECT mkt.id,
         mkt.name,
         count(distinct port.id_mp) as participating_CRRAHs,
         to_char(count(bid.id), '999,999,999,999') as bidcount
    from hedgeuser.ftr_market mkt
   inner join hedgeuser.ftr_portfolio port
      on (mkt.ID = port.id_market and port.credit_status = 4)
   inner join hedgeuser.ftr_ptp_bid bid
      on (port.id = bid.id_portfolio)
   where mkt.id >= 7000
   group by mkt.id, mkt.name),

results as
 (select id_market, ftr_option, class, sum(transaction_amount) as revenue
    from hedgeuser.ftr_out_transaction
   where id_market >= 7000
   group by id_market, ftr_option, class
   order by ftr_option)

select distinct CPs.id                      as Auction_ID,
                CPs.name                    as Auction_Name,
                CPs.participating_CPs       as participating_CPs,
                CPs.final_locked_credit     as Submitted_Credit,
                CRRAHs.participating_CRRAHs as Num_Participating_CRRAHs,
                CRRAHs.bidcount             as Submitted_Transactions
  from results
 inner join CPs
    on CPs.id = results.id_market
 inner join CRRAHs
    on CRRAHs.id = CPs.id
 order by auction_id desc

                    """
    )

    df.columns = [
        "Auction ID",
        "Auction Name",
        "# Participating CPs",
        "Final Locked Credit",
        "# Participating CRRAHs",
        "Submitted Transactions",
        # "OBL Revenue",
        # "OPT Revenue",
        # "Total Revenue",
    ]
    return df


if __name__ == "__main__":
    run_analysis_query("2024.AUG.Monthly.Auction")
