from ercotdb import Database
import streamlit as st

prod = Database(dbname="PR07CRR")


@st.cache_data
def get_recent_auctions(num: int = 15) -> list:
    df = prod.query(
        f"""
    select id, name
    from HEDGEUSER.FTR_MARKET t
    where name not like '%llocation%'
    order by id desc
    fetch first {num} rows only
    """
    )
    print(f"Running get_recent_auctions function")
    return df


if __name__ == "__main__":
    get_recent_auctions(6)
