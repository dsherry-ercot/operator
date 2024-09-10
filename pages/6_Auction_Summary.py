import streamlit as st
from AuctionSummary import SQL
from components.SQLqueries.get_auction_list import get_recent_auctions
from automations.Auction_Summary import main

# Initializing state
if "auction" not in st.session_state:
    st.session_state.auction = "Unspecified"

if "summarize" not in st.session_state:
    st.session_state.summarize = False


# Callback functions
def run_summary():
    st.session_state.summarize = True


# Title
st.title("Summarize Auction")
# st.markdown(st.session_state.summarize)
st.markdown("______")

st.markdown("#### Choose Auction name:")
auction_list = get_recent_auctions(15)["name"]
st.session_state.auction = st.selectbox(
    "Shall be hidden",
    auction_list,
    label_visibility="hidden",
)

st.write("You selected:", st.session_state.auction)

# Input Auction Name

st.markdown("______")

# Configure Auction
st.markdown("#### Click this button to run auction summarization")


first_button = st.button(
    "Summarize!", key="validatekey", on_click=run_summary
)

# State handling
if first_button and st.session_state.summarize:
    with st.spinner("Wait for it..."):
        main.summarize(st.session_state.auction)

        # trigger_btn = ui.button(text="Trigger Button", key="trigger_btn_1")
        # ui.alert_dialog(
        #     show=first_button,
        #     title="Enter real Auction name",
        #     description="and remember to hit 'Return' key",
        #     confirm_label="OK",
        #     cancel_label="Cancel",
        #     key="alert_dialog_1",
        # )

st.markdown("______")

# st.markdown(st.session_state)
