import pandas as pd
import streamlit as st

# Initializing empty dataframes. So if statement below doesn't throw error
df1 = pd.DataFrame()
df2 = pd.DataFrame()


st.subheader('Upload first Excel file')
uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx', key="first")
if uploaded_file:
    st.markdown('---')
    df1 = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df1, use_container_width=True, hide_index=True)

st.subheader('Upload second Excel file')
uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx', key="second")
if uploaded_file:
    st.markdown('---')
    df2 = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df2, use_container_width=True, hide_index=True)

st.markdown('---')


if not df1.empty and not df2.empty:
    st.markdown("### Differences:")
    comparison = df1.compare(df2, result_names=("First Upload:", "Second Upload:"), align_axis=0)
    st.write(comparison)






