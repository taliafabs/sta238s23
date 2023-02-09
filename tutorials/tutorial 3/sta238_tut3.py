import statistics
from cmath import sqrt

data = [.83, .88, .88, 1.04, 1.09, 1.12, 1.31, 1.48,
        1.49, 1.59, 1.62, 1.65, 1.71, 1.76, 1.83]

# no need for this w the statistics import
# def mean(sample: list[float]) -> float:
#     """Return the mean
#     """
#     total = 0
#     for observation in sample:
#         total += observation
#     return total / len(sample)


# (i)
mu = statistics.mean(data)
n = len(data)
s = statistics.stdev(data)
se = s / (sqrt(n))

print("part i")
print("sample mean: ", mu)
print("sample standard deviation: ", s)
print("square error: ", se)


# data <- c()
#
# # question 1
#
# # (i)
# mu <- mean(data)
#
# # (ii)
# n <- length(data)
# s <- sd(data)
# se <- s/sqrt(n)
#
# # (iii)
# t <-  s*qnorm(0.9) + mu
#
# # (iv)
# pnorm((1.5 - mu)/s)
