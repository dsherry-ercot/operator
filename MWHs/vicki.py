import pandas as pd

lst = ["otherkey", "value", "value2"]


for index, val in enumerate(lst):
    if "val" in val:
        print(index)

print(lst, end=False)
