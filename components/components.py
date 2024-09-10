# import streamlit as st
from ercotdb import Database

# -- Get Auction Name --


# @st.cache_data
def get_auction_names():
    prod = Database(dbname="PR07CRR")
    auction_query = prod.query(
        """select unique(name), DATA_PUBLISH_DATE from HEDGEUSER.FTR_MARKET Order BY DATA_PUBLISH_DATE desc"""
    )
    return auction_query["name"]


if __name__ == "__main__":
    # print(get_month_folder_name.__doc__)
    pass
