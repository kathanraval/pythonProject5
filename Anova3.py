import pandas as pd
import numpy as np
import math
from scipy import stats
import scipy
import statsmodels.api as sm
from statsmodels.formula.api import ols
from matplotlib import pyplot as plt
from statsmodels.stats.anova import anova_lm

df= pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5/_RBD.xlsx")
print(df)
df.columns = [col.strip() for col in df.columns]
data= pd.melt(df.reset_index(),id_vars=["index"],value_vars=["System A","System B","System C"])
data.columns=["blocks","treatments","value"]
model =ols("value ~ C(blocks)+C(treatments)",data=data).fit()
anova_table = sm.stats.anova_lm(model,type=1)
print(anova_table)

df1 = pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5/rbd2.xlsx")
print(df1)
df1.columns=[col.strip() for col in df1.columns]
data1 = pd.melt(df1.reset_index(),id_vars=["index"],value_vars=["chem1","chem2","chem3","chem4"])
data.columns=["blocks","treatments","value"]
model = ols("value ~C(blocks) + C(treatments)",data=data).fit()
aov_table = sm.stats.anova_lm(model, typ=1)
print(aov_table)

df2= pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5/Twoway.xlsx")
print(df2)
df2.columns=[col.strip() for col in df2.columns]
formula = "Value ~C(college)+C(prep_pro)+C(college):C(prep_pro)"
model = ols(formula,df2).fit()
aov_table = anova_lm(model,typ=2)
print(aov_table)