import pandas as pd
import glob
import os

mine = rf"C:\Users\dsherry\Desktop\2023 data files"
james = rf"Q:\Posting Data\Public Release of Protected Data\2023 data files"

print("Dan's folder:")
for file in os.listdir(mine):
    if ".xlsx" in file:
        file_path = os.path.join(mine, file)
        df = pd.read_excel(file_path)
        print(file, df.info, "(rows, columns)")

print("James's folder:")
for file in os.listdir(james):
    if ".xlsx" in file:
        file_path = os.path.join(james, file)
        df = pd.read_excel(file_path)
        print(file, df.info, "(rows, columns)")
