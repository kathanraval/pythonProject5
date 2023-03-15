
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

df = pd.read_csv("C:/Users/LENOVO/PycharmProjects/pythonProject5\Data 2.csv")
fd = pd.read_csv("C:/Users/LENOVO/PycharmProjects/pythonProject5\G8_DATASETc.csv")
gp = pd.read_csv("D:/Kathan/Au Assignment/Data Analysis\Data1.csv")
lp = pd.read_csv("C:/Users/LENOVO/PycharmProjects/pythonProject5\G8_DATASET.csv")
jj = pd.read_csv("C:/Users/LENOVO/PycharmProjects/pythonProject5\gapminder - gapminder.csv")


print(fd.shape)
print("")
print(fd.columns)
print("")
print(fd.head())
print("")
print(fd.dtypes)
print("")
print(fd.info)
print("")


print(df.shape)
print("")
print(df.columns)
print("")
print(df.head())
print("")
print(df.dtypes)
print("")
print(df.info)


country_df = df["country"]
print(country_df.head())
print("")
print(country_df.tail())
print("")



print(fd.shape)
subset = fd[["Sr. No.","Education","Joining Year",]]
print(subset.head())
print("")
print(subset.tail())
print("")
print(fd.loc[0])
print("")
print(fd.loc[49])

print(jj.shape)
print("")
print(jj.columns)
print("")
print(jj.head())
print("")
print(jj.dtypes)
print("")
print(jj.info)


subset = jj[["country",	"year",	"population",	"continent",	"life_exp"	,"gdp_cap"]]
print(subset.head())
print("")
print(subset.tail())
print("")
print(jj.loc[0])
print("")
print(jj.loc[99])
print("")
print(jj.tail(n=1))
print("")
print(jj.loc[[0,99,99]])
print("")
print(jj.iloc[-1])
subset = jj.loc[:,["year","population"]]
print("")
print(subset.head())
small_range = list(range(5))
subset1 = jj.iloc[:,small_range]
print(subset1.head())
print("")
print(jj.loc[42,"country"])
print("")
print(jj.iloc[42,1])
print("")
print(jj.iloc[[0,9,99],[1,2,3]])
print("")
print(jj.loc[[0,9,99],["country","year","population"]])
print("")
print(jj.loc[10:13],["country","year","population"])
print("")
print(jj.groupby("population")["life_exp"].mean())
multgrp_var = jj.\
    groupby(["population","country"])\
    [["life_exp","gdp_cap"]].\
    mean()
print(multgrp_var)
print("")
flat = multgrp_var.reset_index()
print(flat.head(15))
print("")
print(jj.groupby("continent")["country"].nunique())
global_yearly = jj.groupby("continent")["life_exp"].mean()
pl.plot(global_yearly)
pl.show()
