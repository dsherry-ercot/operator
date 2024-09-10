from ercotdb import Database
import streamlit as st
from components.SQLqueries.get_auction_list import get_recent_auctions

crr = Database("pr07crr")


def get_dropdown():
    results = get_recent_auctions()["name"]
    dropdown = st.selectbox(
        "Auction Name",
        results,
        index=None,
        placeholder="Select Auction",
    )
    return dropdown


if __name__ == "__main__":
    print(get_recent_auctions())
