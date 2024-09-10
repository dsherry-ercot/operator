import streamlit as st
from automations import posting_files
import streamlit_shadcn_ui as ui
import os
import shutil

username = os.getlogin()

# Initializing state
if "folder" not in st.session_state:
    st.session_state.folder = "Unspecified"

if "configure" not in st.session_state:
    st.session_state.configure = False

if "attach" not in st.session_state:
    st.session_state.attach = False


# Callback functions
def configure_auction():
    st.session_state.configure = True


# Title
st.markdown("### 6.3.1: Publish the CRR Network Model")
st.markdown("______")

# Input Auction Name
st.markdown("#### Input posting files folder:")
st.write(username)
folder_path = st.text_input("Input folder path (sent in email by model builder)")
# Scan the folder with files.
file_paths = []
if os.path.isdir(folder_path):
    for fn in os.listdir(folder_path):
        fp = f"{folder_path}/{fn}"
        if os.path.isfile(fp):
            file_paths.append(fp)
st.write(file_paths)


def copy_files():
    parent_dir = rf"C:\Users\{username}\Downloads"
    directory = r"DanTester"
    path = os.path.join(parent_dir, directory)
    if not os.path.exists(path):
        os.mkdir(path)
        for fp in file_paths:
            shutil.copy(fp, path)
        st.session_state.folder = "DanTester"
    else:
        print("Directory already exists")


st.markdown("______")

# Configure Auction
st.markdown(
    "#### 1. Clicking this button will make a copy of posting files, rename them, add KML readme, and zip them. It will be saved in your Downloads."
)
st.markdown(
    '###### Move the newly made zip folder into the proper "Auction Models Posted to MIS" folder'
)
st.write(f"Check downloads for folder: **{st.session_state.folder}**")

first_button = st.button("Run Script!", key="configurekey", on_click=copy_files)
st.markdown("______")


# State handling
# if first_button and st.session_state.configure:
#     if len(st.session_state.nan) > 3:
#         define_configure_market.dcm(st.session_state.nan)
#     else:
#         # trigger_btn = ui.button(text="Trigger Button", key="trigger_btn_1")
#         ui.alert_dialog(show=first_button, title="Enter real Auction name", description="and remember to hit 'Return' key", confirm_label="OK", cancel_label="Cancel", key="alert_dialog_1")

# if second_button and st.session_state.attach:
#     define_configure_market.attach_data_cases(st.session_state.nan)
