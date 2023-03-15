import pandas as pd
import numpy as np
import math
from scipy import stats
import scipy
import statsmodels.api as sm
from statsmodels.formula.api import ols
from matplotlib import pyplot as plt

data = pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5\oneway.xlsx")
print(data)
data.columns = [col.strip() for col in data.columns]
data_new = pd.melt(data.reset_index(), id_vars=["index"], value_vars=["Black Board", "Case Presentation", "PPT"])
data_new.columns = ["index", "treatments", "value"]
print(data_new)
model= ols('value ~ C(treatments)', data=data_new).fit()
anova_table= sm.stats.anova_lm(model,type=1)
print(anova_table)

print("")
print("")
print("")
fivepercent = [7,8,15,11,9,10]
tenpercent=[12,17,13,18,19,15]
fifteenpercent=[14,18,19,17,16,18]
twentypercent=[19,25,22,23,18,20]
box_plot=[fivepercent,tenpercent,fifteenpercent,twentypercent]
plt.boxplot(box_plot)
plt.show()
print(scipy.stats.f_oneway(fivepercent,tenpercent,fifteenpercent,twentypercent))
df =pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5\Tensile strength of paper.xlsx")
print(df)
df.columns=[col.strip() for col in df.columns]
data_r1=pd.melt(df.reset_index(), id_vars=["index"] , value_vars=["hardwood concentration 5%","hardwood concentration 10%","hardwood concentration 15%","hardwood concentration 20%"])
data_r1.columns=["index","treatments","value"]
model=ols("value ~ C(treatments)",data=data_r1).fit()
print(model.summary())
aov_table = sm.stats.anova_lm(model,typ=1)
print(aov_table)
t = -1*scipy.stats.t.ppf(0.025,20)
n =6
MSE = 6.5083
lsd = t*math.sqrt(2*MSE/n)
print(lsd)
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
mc = MultiComparison(data_r1["value"],data_r1["treatments"])
mcresult = mc.tukeyhsd(0.05)
print(mcresult.summary())

df3 = pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5\cotton weight.xlsx")

# df3.columns=[col.strip() for col in df3.columns]
# data_1 = pd.melt(df3.reset_index(),id_vars=["index"],value_vars=["cotwt.15","cotwt.20","cotwt.25","cotwt.30","cotwt.35"])
# data_1.columns=["id","value","treatments"]
# data_1["value"] = data_1["value"].astype(float)  # Convert the "value" column to float data type
# mc=MultiComparison(data_1["value"],data_1["treatments"])
# mcresult1=mc.tukeyhsd(0.05)
# print(mcresult1.summary())

df4 = pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5\cotton weight.xlsx")
df4.columns=[col.strip() for col in df4]