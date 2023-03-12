from cmath import sqrt

import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import t

n1 = 15
n2 = 15

y1 = 446
y2 = 544

s1 = 42
s2 = 45

print(y1-y2)

# df = n1 + n2 - 2
#
# s2p = (14*42**2 + 14*45**2)/28
# pooled_se = sqrt(s2p*(2/30))
# delta = y1 - y2
#
# lb95 = delta - t.ppf(0.975,df)*pooled_se
# ub95 = delta + t.ppf(0.975,df)*pooled_se
#
# print(delta)



