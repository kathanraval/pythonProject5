import pandas as pd
import numpy as np
import math
import matplotlib as mpl
import seaborn
import sns
import seaborn as sns
from scipy import stats
import scipy
import statsmodels.api as sm
import statsmodels.formula.api as sm_formula
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from scipy import stats
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import summary_table

# data =pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5/reg2.xlsx")
# print(data.columns)
# x=data["Hydrocarbon level"]
# y=data["O2"]
# plt.figure()
# sns.regplot(data = data, x=x, y=y)
# plt.scatter(np.mean(x), np.mean(y), color="green")
# plt.show()


tbl = pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5/regr.xlsx")
print(tbl.columns)

# tbl.plot("TV Ads","car Sold",style="o")
# plt.ylabel("car Sold")
# plt.title("sales in several UK region")
# plt.show()
t=tbl["TV Ads"]
c=tbl["car Sold"]
t=sm.add_constant(t)
model=sm.OLS(c,t)
result1=model.fit()
print(result1.summary())

data = pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5/HARDNESS.xlsx")
print(data.columns)
x=data["Hardness"].values.reshape(-1,1)
y=data["Tensile strength"].values.reshape(-1,1)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=88)
x_train.shape,x_test.shape,y_train.shape,y_test.shape
print(len(x_train))
print(len(x_test))
reg =LinearRegression()
reg.fit(x_train,y_train)
print(reg.intercept_)
print(reg.coef_)
y_predict=reg.predict(x_test)
print(y_predict)
print(mean_squared_error(y_test,y_predict))
print(reg.score(x_test,y_test))
print(reg.score(x_train,y_train))

data = pd.read_excel("C:/Users/LENOVO/PycharmProjects/pythonProject5/lrm.xlsx")
print(data.columns)
data.plot("Student_Population","Sales",style="o")
plt.ylabel("Ice Cream Sales")
plt.title("Sales")
plt.show()

st_pop=data["Student_Population"]
sales=data["Sales"]
st_pop=sm.add_constant(st_pop)
model1=sm.OLS(sales,st_pop)
result1=model1.fit()
print(result1.summary())

x=data["Student_Population"].values.reshape(-1,1)
y=data["Sales"].values.reshape(-1,1)
reg=LinearRegression()
reg.fit(x,y)
print(reg.intercept_[0],reg.coef_[0][0])

a=data["Student_Population"]
b=data["Sales"]
plt.figure()
sns.regplot(data=data,x=a,y=b,fit_reg=True)
plt.scatter(np.mean(a),np.mean(b),color="red")
plt.show()

st,data,ss2=summary_table(result1,alpha=0.05)
fittedvalues=data[:,2]
predict_mean_se=data[:,3]
predict_mean_ci_low,predict_mean_ci_upp=data[:,4:6].T
predict_ci_low,predict_ci_upp=data[:,6:8].T


X=sm.add_constant(a)
fig,ax=plt.subplots(figsize=(8,6))
ax.plot(a,b,"o",label="data")
ax.plot(X,fittedvalues,"r--",label="OLS")
ax.plot(X,predict_ci_low,"b--")
ax.plot(X,predict_ci_upp,"b--")
ax.plot(X,predict_mean_ci_low,"g--")
ax.plot(X,predict_mean_ci_upp,"g--")
ax.legend(loc="best")
plt.show()