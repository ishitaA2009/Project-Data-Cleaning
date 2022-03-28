import csv
import pandas as pd

df=pd.read_csv("final.csv")
print(df.shape)

del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df.to_csv("main.csv")