import streamlit as st
from automations.SAS_Tool import main
from components.SQLqueries.get_auction_list import get_recent_auctions

# Initializing state
if "auction" not in st.session_state:
    st.session_state.auction = "Unspecified"

if "validate" not in st.session_state:
    st.session_state.validate = False


# Callback functions
def run_validations():
    st.session_state.validate = True


# Title
st.title("Validate Auction")
# st.markdown(st.session_state.validate)
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

# st.session_state.auction = option

st.markdown("______")

# Configure Auction
st.markdown("#### 1. Click this button to run auction validations")

# st.text(st.session_state)


first_button = st.button(
    "Run Validations!", key="validatekey", on_click=run_validations
)

# State handling
if first_button and st.session_state.validate:
    with st.spinner("Wait for it..."):
        main.get_files(st.session_state.auction)

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
