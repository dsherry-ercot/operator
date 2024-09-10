import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# Proto")
st.sidebar.header("Dan Prototype yuh")
st.write(
    """This is my first attempt at a useful page"""
)


@st.cache_data
def get_dan_data():
    df = pd.read_csv(r"Q:\Users\dsherry\2023_MAR_PST-miniTab_All.csv", header=1, nrows= 200)
    return df #.set_index("Region")



df = get_dan_data()
df
st.bar_chart(df, y="Amount $", use_container_width=True)

    
    # countries = st.multiselect(
    #     "Choose countries", list(df.index), ["China", "United States of America"]
    # )
    # if not countries:
    #     st.error("Please select at least one country.")
    # else:
    #     data = df.loc[countries]
    #     data /= 1000000.0
    #     st.write("### Gross Agricultural Production ($B)", data.sort_index())

    #     data = data.T.reset_index()
    #     data = pd.melt(data, id_vars=["index"]).rename(
    #         columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
    #     )
#     chart = (
#         alt.Chart(df)
#         .mark_area(opacity=0.3)
#         .encode(
#             x="year:T",
#             y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
#             # color="Region:N",
#         )
#     )
#     st.altair_chart(chart, use_container_width=True)
# except URLError as e:
#     st.error(
#         """
#         **This demo requires internet access.**
#         Connection error: %s
#     """
#         % e.reason
#     )