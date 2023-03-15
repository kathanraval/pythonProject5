import scipy
import math
import pandas as pd
import numpy as np
from scipy import stats
import chess
# print(stats.norm.cdf(-1.46))
# print(1-stats.norm.cdf(2.29))
# print(stats.norm.ppf(0.1))
# print(stats.norm.ppf(0.95))
# print(1-stats.norm.cdf(1.09))
# print((1-stats.norm.cdf(2.74)))
x=[10,12,21,22,24,18,15]
print(stats.ttest_1samp(x,15))
x =[13,8,10,10,8,9,10,11,6,8,12,11,11,12,10,12,7,10,11,8]
print(stats.ttest_1samp(x,10))
from statsmodels.stats.proportion import proportions_ztest
count = 67
samplesize = 120
p = 0.5
a=proportions_ztest(count,samplesize,p)
print(a)
x = 48.5
mu=50
sem = 0.79

def z_vaule(x,mu,sem):
    z = (x-mu)/sem
    if (z<0):
        alfa = stats.norm.cdf(z)
    else:
        alfa = 1-stats.norm.cdf(z)
    print(alfa)

z_vaule(51.5,50,0.79)

def type_2(mu1,mu2,sigma,n,alfa):
    z = stats.norm.ppf(alfa)
    xbar=(mu1)+(z*sigma/np.sqrt(n))
    z2 = (xbar-mu2)/(sigma/np.sqrt(n))
    if (mu1>mu2):
        beta = 1-stats.norm.cdf(z2)
    else:
        beta = stats.norm.cdf(z2)
    print(beta)

type_2(8.3,7.4,3.1,60,0.05)
type_2(12,11.99,0.1,60,0.05)

def z_and_p (x1,x2,sigma1,sigma2,n1,n2):
    z= (x1-x2)/(math.sqrt(((sigma1**2)/n1)+((sigma2**2)/(n2))))
    if(z<0):
        p = stats.norm.cdf(z)
    else :
        p= 1-stats.norm.cdf(z)
    print(z,p)

z_and_p(121,112,8,8,10,10)
print(stats.t.ppf(0.025,13))# critical t value
metro = [3,7,25,10,15,6,12,25,15,17]
rural =[48,44,40,38,33,21,20,12,1,18]
print(stats.ttest_ind(metro,rural,equal_var=False))
print(stats.ttest_rel(metro,rural))
#def two_samp_prop(p1,p2,n1,n2):
    # p_pool = ((p1*n1)+(p2*n2))/(n1+n2)
    # s_sq = (p_pool)*(1-p_pool)*((1/n1)+(1/n2))
    # s = math.sqrt(s_sq)
    # z = (p1-p2)/s
    # if(z<0):
    #     p_val = stats.norm.cdf(z)
    # else:
    #     p_val = 1-stats.norm.cdf(z)
    # print(z,p_val*2)
# two_samp_prop(0.27,19,100,100)

print(scipy.stats.f.ppf(q=1-0.05,dfn=15,dfd=10))
print(scipy.stats.f.ppf(q=0.05,dfn=15,dfd=10))

x=[3,7,25,10,15,6,12,25,15,7]
y=[48,44,40,38,33,21,20,12,1,18]
F=(np.var(x))/(np.var(y))
dfn = len(x)-1
dfd = len(y)-1
p_val = scipy.stats.f.ppf(F,dfn,dfd)
print(p_val)
def samplesize(alfa,beta,mu1,mu2,sigma):
    z1 = -1*stats.norm.ppf(alfa)
    z2 = -1*stats.norm.ppf(beta)
    n = (((z1+z2)**2)*(sigma**2))/((mu1-mu2)**2)
    print(n)

a=[4,3,2]
b=[2,4,6]
c=[2,1,3]
print(stats.f_oneway(a,b,c))

