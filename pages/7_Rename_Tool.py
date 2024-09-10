import streamlit as st
from automations.Rename.main import main
from components.SQLqueries.get_auction_list import get_recent_auctions

# Initializing state
if "path" not in st.session_state:
    st.session_state.path = "Unspecified"

if "rename" not in st.session_state:
    st.session_state.rename = False


# Callback functions
def run_rename():
    st.session_state.rename = True


# Title
st.title("Rename tool")
# st.markdown(st.session_state.summarize)
st.markdown("______")

# Input Auction Name
st.markdown('#### Input path to Network Model folder:')
st.session_state.path = st.text_input(
    "Hiding this with flag", placeholder="Input path to Network Model files", label_visibility="collapsed", key="path_key")
st.write('Examples:    \n Q:\Posting Data\Long-Term Auctions\LTAS23 (2024.2nd6 - 2027.1st6)\\2027.1st6.AnnualAuction.Seq6 ')
st.markdown('______')


st.write("You selected:", st.session_state.path)

st.markdown("______")

# Configure Auction
st.markdown(
    "#### Click this button to rename and zip files into my Downloads folder")


first_button = st.button(
    "Rename!", key="validatekey", on_click=run_rename
)

# State handling
if first_button and st.session_state.rename:
    with st.spinner("Wait for it..."):
        main(st.session_state.path)
    st.markdown("Check downloads folder!")

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
