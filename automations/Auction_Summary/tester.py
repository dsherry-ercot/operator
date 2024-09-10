import pandas as pd

df = pd.DataFrame(
    {"Transactions Submitted": [373359, 33321]}
)

df["Transactions Submitted"].apply(lambda x:  "{:,}".format(x))

print(df.dtypes)
