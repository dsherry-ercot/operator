import streamlit as st
from automations import file_explorer

st.set_page_config(page_title="Operator App", page_icon="👋", layout="wide")

st.write("# A CRR Market Operator Application!")

st.sidebar.success("Select a tab above!")

col1, col2 = st.columns([2, 10])
with col1:
    st.button("Open Monthly TC Logs", on_click=file_explorer.open_monthly_tc)
with col2:
    st.button("Open Annual TC Logs", on_click=file_explorer.open_annual_tc)

st.markdown(
    """
    
    ### Here are some important links:
    - [CRR SharePoint site](https://ercot.sharepoint.com/sites/departments/carr/CRR/SitePages/Home.aspx), here you'll find:
        - The Activity Calendar, Completion Logs, Desk Procedures, and Market Operator training material
    - [CRR - Market Operator Interface](https://mis.ercot.com/moi-ercot-ihedge/#/market/auction), Production link
        - [MOTE env.](https://testmis.ercot.com/siteminderagent/cert/1706556062/smgetcred.scc?TYPE=16777244&REALM=-SM-00--TOP%20[13%3a21%3a02%3a8954]&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-saGLw6uxCYhOUBN1cqjLdX6Gg7%2bBONBjfwfoQtaR3m7jSYbAyVpzeUcUhlyTQypN&TARGET=-SM-https%3a%2f%2ftestmis%2eercot%2ecom%2fmoi--ercot--ihedge%2f#/)
        - [iTest env.](https://itestmis.ercot.com/siteminderagent/cert/1706555920/smgetcred.scc?TYPE=16777244&REALM=-SM-00--TOP%20[13%3a18%3a40%3a140174847643894]&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=4pyeLBLhaaph1xsZUujyhSuxmb1gywPqVPWAPE1adCbtaPDNdFjkEacMUt75lsBV&TARGET=-SM-https%3a%2f%2fitestmis%2eercot%2ecom%2fmoi--ercot--ihedge%2f#/)
        - [FAT env.](https://fatsso.ercot.com/siteminderagent/cert/1706556029/smgetcred.scc?TYPE=16777244&REALM=-SM-F--TOP%20[13%3a20%3a29%3a139788300582993]&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=I3Iqm6PkmyoZvxrhISrPLjDJIUQwH808HqdoXcyhybcyCgMyxSQgHxLDg8oxXJ45&TARGET=-SM-https%3a%2f%2ffatsso%2eercot%2ecom%2fmoi--ercot--ihedge%2f#/)
    - [IAM Certifications](https://iam.ercot.com/certifications/list/), to check out what certifications you have pending
    - [Siebel](https://eenergy.ercot.com/siebel/app/eEnergyADSI/ENU?SWECmd=GotoView&SWEView=ERCOT+Customer+Account+List+View&SWERF=1&SWEHo=eenergy.ercot.com&SWEBU=1&SWEApplet0=ERCOT+Customer+Account+List+Applet&SWERowId0=1-11LUP9T&_tid=1709325342), for market participant information
    - [ERCOT Service Portal](https://ercot.servicenowservices.com/sp?id=index), to create a ticket or request software, etc.


"""
)
