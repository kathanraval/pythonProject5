import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/LENOVO/PycharmProjects/pythonProject5\gapminder2.xlsx')

print(df)
print("")
x = df["Total"]
print(np.mean(x))
print("")
print(np.median(x))
import scipy
from scipy import stats
jj = stats.mode(x, keepdims=False)
print(jj)
print("")
a = np.array([1,2,3,4,5])
p = np.percentile(a,50)
print(p)
print("")
for i in range(10,20,2):
    print(i, end=",")
def greet():
    print("")
    print("Hi")
    print("Good Morning")

greet()
print("")
data = [1,3,89,76,45,233,456,999]
# print(min(data))
# print(max(data))
def rangef (data):
    print("i am called")
    min1 = min(data)
    max2 = max(data)
    print(max2-min1)
    return ()

rangef(data)

a = np.array([1,2,3,4,5])
q1 = np.percentile(a,25)
print(q1)

a = np.array([1,2,3,4,5])
q2 = np.percentile(a,50)
print(q2)

a = np.array([1,2,3,4,5])
q3 = np.percentile(a,75)
print(q3)

print(np.var(x))

import statistics
print(statistics.pstdev(x))
print(statistics.stdev(x))

from scipy.stats import skew
print(skew(x))

plt.boxplot(x,sym=None)
plt.show()
plt.bar(x,100,50,bottom=None)
plt.show()