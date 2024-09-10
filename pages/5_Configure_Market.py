import streamlit as st
from automations import define_configure_market
import streamlit_shadcn_ui as ui

# Initializing state
if "nan" not in st.session_state:
    st.session_state.nan = "Unspecified"

if 'configure' not in st.session_state:
    st.session_state.configure = False

if 'attach' not in st.session_state:
    st.session_state.attach = False

# Callback functions


def configure_auction():
    st.session_state.configure = True


def attach_datacases():
    st.session_state.attach = True


# Title
st.markdown('### 6.1.3: Define and configure market')
st.markdown('______')

# Input Auction Name
st.markdown('#### Input Auction name:')
st.session_state.nan = st.text_input(
    "Hiding this with flag", placeholder="Input Auction Name Here", label_visibility="collapsed", key="nan_key")
st.write('Examples:    \n2024.APR.Monthly.Auction    \n2026.2nd6.AnnualAuction.Seq6')
st.markdown('______')

# Configure Auction
st.markdown(
    '#### 1. Clicking this button will open up the MOI and populate most of the form for you!')
st.markdown('You will still need to verify everything is accurate and press "Save" yourself. Input an auction name above and press enter before running script.')
st.write(f"About to create an auction for: **{st.session_state.nan}**")

first_button = st.button(
    'Run Script!', key="configurekey", on_click=configure_auction)
st.markdown('______')

# Create Datacases
# st.markdown('#### 2. Create datacases for newly created auction.')
# st.markdown('You will still need to verify everything is accurate and press "Save" yourself. Input an auction name above and press enter before running script.')
# second_button = st.button('Run Script!', key="attach_datacaseskey", on_click=attach_datacases)

# State handling
if first_button and st.session_state.configure:
    if len(st.session_state.nan) > 3:
        define_configure_market.dcm(st.session_state.nan)
    else:
        # trigger_btn = ui.button(text="Trigger Button", key="trigger_btn_1")
        ui.alert_dialog(show=first_button, title="Enter real Auction name", description="and remember to hit 'Return' key",
                        confirm_label="OK", cancel_label="Cancel", key="alert_dialog_1")

# if second_button and st.session_state.attach:
#     define_configure_market.attach_data_cases(st.session_state.nan)
