import scipy
import numpy as np
from scipy.stats import binom, uniform, poisson, norm, hypergeom, expon
print(binom.pmf(k=19,n=25,p=0.65))
print(binom.cdf(2,20,0.06))
print(binom.pmf(k=19,n=20,p=0.4))


print(poisson.pmf(3,2))
print(poisson.pmf(5,3.2))
prob = poisson.cdf(7,3.2)
print(prob)
more_7 = 1-prob
print(more_7)
print(poisson.pmf(10,6.4))
u = np.arange(27,40,1)
print(uniform.mean(loc= 27,scale = 12))
print(uniform.cdf(np.arange(30,36,1),loc =27, scale = 12))
print(uniform.mean(loc=200,scale =982))
print(uniform.std(loc=200,scale = 982))
val,m,s = 68,65.5,2.5
print(norm.cdf(val,m,s))
print(1-norm.cdf(700,494,100))
print(norm.ppf(0.95))
print(norm.ppf(1-0.6722))
print(hypergeom.sf(0,18,3,12))
pval = hypergeom.cdf(1,18,5,11)
print(pval)
print(1/1.38)
expon.cdf(0.75,0,(1/1.38))
