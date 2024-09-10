import streamlit as st
import time
from ercotdb import Database

prod = Database("PR07CRR")


st.write("## HEDGEUSER.FTR_MARKET")
option = st.selectbox(
    "Auction Type?",
    ("Month", "Annual"),
    index=None,
    placeholder="Select Auction type..",
)
start = time.time()

col1, col2 = st.columns(2)
with col1:
    with st.spinner("Wait for it..."):
        if not option:
            df = prod.query(
                """select id, name
                            from HEDGEUSER.FTR_MARKET 
                            order by name desc"""
            )
        else:
            df = prod.query(
                f"""select id, name 
                            from HEDGEUSER.FTR_MARKET 
                            where name like '%{option}%'
                            order by name desc"""
            )
    st.dataframe(
        df,
        hide_index=True,
        height=550,
    )

with col2:
    row_count = len(df.index)
    st.metric(label="No. of rows", value=int(row_count))

load_time = "{:.3f}".format(time.time() - start)
st.write(f"Loading time: {load_time} seconds")

msg = st.success(" Done!", icon="🎉")

st.button("Rerun")
