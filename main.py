import pandas as pd


df = pd.read_csv("./database/ClientesBanco.csv", sep=",", encoding="latin1")
df.to_excel("ClientesBanco.xlsx", index=False)
print(df.head())