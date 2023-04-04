import statistics

population1 = [19, 25, 31, 52, 49, 34, 59, 47, 17, 51]
population2 = [24, 27, 36, 53, 55, 34, 66, 51, 20, 55]

n1 = len(population1)
y1 = (sum(population1)) / n1
svar1 = statistics.variance(population1)
s1 = statistics.stdev(population1)

n2 = len(population2)
y2 = (sum(population2)) / n2
svar2 = statistics.variance(population2)
s2 = statistics.stdev(population2)

num_pairs = n1 = n2

differences = []
pair_index = 0
for pair_index in range(num_pairs):
    pair_diff = population1[pair_index] - population2[pair_index]
    differences.append(pair_diff)
    pair_index += 1

mean_differences = (sum(differences)) / num_pairs

print(differences)
print("mean differences: ", mean_differences)
print("y1 = ", y1)
print("y2 = ", y2)
print("y1 - y2 = ", y1-y2)
print("s1^2 = ", svar1)
print("s2^2 = ", svar2)
print("s1 = ", s1)
print("s2 = ", s2)