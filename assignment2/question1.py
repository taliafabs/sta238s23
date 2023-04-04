from cmath import sqrt

import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import t

# 1(a)
# n1 = 15
# n2 = 15
#
# y1 = 446
# y2 = 534
#
# s1 = 42
# s2 = 45
#
# d = y1-y2
# s2p = ((n1 - 1)*s1**2 + (n2 - 1)*s2**2)/(n1 + n2 - 2)
#
# lb95 = d - (t.ppf(0.025, 28) * sqrt(s2p * (2/15)))
# ub95 = d + t.ppf(0.025, 28) * sqrt(s2p * (2/15))
# print(t.ppf(0.975, 28))
# print(s2p * (2/15))
# print(lb95)
# print(ub95)


# 1(b)
n1 = 15
n2 = 15

y1 = 548
y2 = 517

s1 = 57
s2 = 52

d = y1-y2
print(d)
s2p = ((n1 - 1)*s1**2 + (n2 - 1)*s2**2)/(n1 + n2 - 2)
print(s2p)

lb95 = d - (t.ppf(0.025, 28) * sqrt(s2p * (2/15)))
ub95 = d + (t.ppf(0.025, 28) * sqrt(s2p * (2/15)))
print(t.ppf(0.025, 28))
print(s2p * (2/15))
print((t.ppf(0.025, 28) * sqrt(s2p * (2/15))))



