import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/LENOVO/PycharmProjects/pythonProject5\gapminder-FiveYearData.csv")
print(df.info)
print("")
print(df.shape)
print("")
print(df.columns)
print("")
print(df.head(n=10))
print("")
print(df.dtypes)
print("")
column = df["country"]
print(column)
print("")
print(column.head(n=7))
column = df[["country","year","pop","continent"]]
print(column.tail(n=8))
print("")
print(df.loc[0])
# returns the row extraction
print("")
print(df.loc[49])
print("")
print(df.loc[[0,99,999]])
print("")
print(df.iloc[[9,99,999]])
print("")
print(df.loc[:,["country","year"]])
# extracts the coloums, ":" is used to extract columns
print("")
range1 = list(range(3))
subset = df.iloc[:,range1]
print(subset.head(n=3))
subset_1 = df.loc[:,["lifeExp","gdpPercap"]]
print("")
print(subset_1.head())
# loc, will be used to integer and label

# iloc, will be used to integer and integer
print("")
print(df.loc[42,"gdpPercap"])
print("")
print(df.loc[33,"pop"])
# loc, first section for row and followed by "column name"
print("")
print(df.iloc[42,5])
# iloc, first section for rows, using number and follwed by column number
print("")
print(df.loc[[0,99,999],["country","year"]])
print("")
print(df.iloc[[0,99,999],[0,1]])
print("")
ronf = df.groupby("country")["lifeExp"].mean()
print(ronf.head(n=3))
print("")
print(df.groupby("country")["lifeExp"].nunique().head(n=3))
yours = df.groupby("continent")["lifeExp"].mean()
plt.plot(yours)
plt.show()

