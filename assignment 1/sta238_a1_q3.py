import statistics
from cmath import sqrt
from scipy.stats import sem
import matplotlib.pyplot as plt
sample = [91, 80, 99, 110, 95, 106, 78, 121,
          106, 100, 97, 82, 100, 83, 115, 104]

n = len(sample)
sample_mean = statistics.mean(sample)
sample_sd = statistics.stdev(sample)
print("sample mean = ", sample_mean)
print("sample_sd = ", sample_sd)


def sample_variance(data: list[int|float], y_bar: float) -> float:
    """Return the sample variance"""
    total = 0
    for y in data:
        total += (y - y_bar)**2
    s_2 = total / (len(data) - 1)
    return s_2


# def standard_error(data: list[int | float]) -> float:
#     """Calculate the standard error of the sample data
#     """
#     n = len(data)
#     y_bar = sum(data) / n
#     sample_var = sample_variance(data, y_bar)
#     se = sqrt(sample_var) / sqrt(n)
#     return se

S2 = sample_variance(sample, sample_mean)
print("S^2 = ", S2)
s = sqrt(S2)
print("s = ", s)

se = sem(sample)
print("se = ", se)
# se = statistics.s

