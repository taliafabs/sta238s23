# part 2

import statistics
from cmath import sqrt
from scipy.stats import sem

data = [83.4, 87.2, 86.1, 81.3, 84.8, 86.0]


def sample_mean(data: list[int | float]) -> float:
    """Return the sample mean
    """
    total = sum(data)
    n = len(data)
    return total / n


def sample_variance(data: list[int|float], y_bar: float) -> float:
    """Return the sample variance"""
    total = 0
    for y in data:
        total += (y - y_bar)**2
    s_2 = total / (len(data) - 1)
    return s_2

# sm = statistics.mean(data)
# sv = statistics.variance(data, sm)
sample_mean = sample_mean(data)
S2 = sample_variance(data, sample_mean)
print(S2)

