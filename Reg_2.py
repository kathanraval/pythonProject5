import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.api import anova_lm
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
# df1=pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5/icecream.xlsx")
# print(df1)
# reg1=ols(formula="Sales~Student_Population",data=df1)
# fit1=reg1.fit()
# print(fit1.summary())
# print(anova_lm(fit1))
# influence =fit1.get_influence()
# resid_student= influence.resid_studentized_external
# print(resid_student)
# plt.figure()
# plt.scatter(df1["Student_Population"],resid_student,color="purple")
# plt.show()
# res = fit1.resid
# probplot=sm.ProbPlot(res,stats.norm,fit=True)
# fig=probplot.qqplot(line="45")
# h=plt.title("qqplot-residual of OLS fit")
# plt.show()

df2=pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5/TRUCKING.xlsx")
print(df2)
plt.scatter(df2["x1"],df2["travel_time"],color="blue")
plt.ylabel("Travel Time")
plt.title("Simple linear regression model with Miles traveled")
plt.show()


plt.scatter(df2["n_of_deliveries"],df2["travel_time"],color="red")
plt.ylabel("Travel Time")
plt.title("Simple linear regression model with number of deliveries")
plt.show()

plt.figure()
plt.scatter(df2["x1"],df2["travel_time"],color="blue")
plt.scatter(df2["n_of_deliveries"],df2["travel_time"],color="red")
plt.ylabel("Travel Time")
plt.title("Multiple regression")
plt.xlabel("Miles traveled in blue and Number of deliveries in Red")
plt.show()

reg1=ols(formula="travel_time~x1",data=df2)
fit1=reg1.fit()
print(fit1.summary())

model1=ols("travel_time~x1+n_of_deliveries",data=df2).fit()
print(model1.summary())