import statistics
from cmath import sqrt

data = [83.4, 87.2, 86.1, 81.3, 84.8, 86.0]

sample_mean = statistics.mean(data)
sample_variance = statistics.variance(data, sample_mean)
print(sample_mean, sample_variance)

def sample_variance(data: list[int|float], y_bar: float) -> float:
    """Return the sample variance"""
    total = 0
    for y in data:
        total += (y - y_bar)**2
    s_2 = total / (len(data) - 1)
    return s_2

S2 = sample_variance(data, sample_mean)
print(S2)
print(sqrt(S2))

confidence_interval = 90.0
alpha = 100*(1 - confidence_interval)
