import streamlit as st
# from components import components
from automations import operator_msg
# Initializing state & Callback functions

# st.session_state

if 'moi' not in st.session_state:
    st.session_state.moi = False

def set_moi():
    st.session_state.moi = True

def set_moi_false():
    st.session_state.moi = False

st.markdown('## 3.6.1: Manage Site Failovers and Maintenance Outages')
st.markdown('______')

default="""We are failing over MIS today from Bastrop to Taylor, beginning at 17:00. I posted the following operator message to the MUI: 

ERCOT will have a planned system maintenance of the Market Information System (MIS) today, January 18, 2024, from 17:00 until 19:30 CPT. During the maintenance, the CRR application can be accessed directly using this URL: https://mis.ercot.com/mui-ercot-ihedge/.

Thanks,
CRR Team
"""

operator_message = st.text_area("Write Operator message here:", height=200, 
                                value=default)

st.markdown('______')
st.markdown('#### Clicking this button will open up the MOI and draft the message you entered above')
st.markdown('You will still need to verify everything is accurate and press "Post Message" yourself.')
st.write("Your message is: ", len(operator_message), "characters")

st.button('Run Script!', key="moi_button", on_click=set_moi)

# while st.session_state.configure:
#     st.success('Starting!')

st.markdown('______')


# State handling

if st.session_state.moi:
    # st.success('Starting!')
    operator_msg.draft_operator_message(operator_message)
    operator_msg.draft_email(operator_message)
    set_moi_false()

# if st.session_state.attach:
#     # st.success('Starting!')
#     define_configure_market.attach_data_cases(st.session_state.nan)
#     st.session_state.attach = False

# need both AH and CP in dropdown
# ftr_message table