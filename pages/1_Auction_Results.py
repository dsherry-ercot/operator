from ercotdb import Database
# pass along Windows credentials
from requests_negotiate_sspi import HttpNegotiateAuth
from pathlib import Path  # info in Week 4 Mastering Python class
import pandas as pd
from getpass import getuser

# import time
import streamlit as st
from components import auction_dropdown
from components.SQLqueries.auction_analysis import run_analysis_query

st.set_page_config(
    layout="wide", page_title="Auction Results"
)  # initial_sidebar_state="collapsed"

getuser()

ROOT_FOLDER = Path(".")
QUERY_FOLDER = ROOT_FOLDER / "query"
DATA_FOLDER = ROOT_FOLDER / "data"
DATA_FOLDER.mkdir(exist_ok=True, parents=True)


st.write("## Auction Results Table")

# auction_selection = auction_dropdown.get_dropdown()
df = run_analysis_query()
st.dataframe(df, hide_index=True, height=1000)
# start = time.time()

#     df["id"] = df["id"].apply(str)
#     st.dataframe(
#         df,
#         hide_index=True,
#         height=750,
#     )
# load_time = "{:.3f}".format(time.time() - start)
# st.write(f"Loading time: {load_time} seconds")
