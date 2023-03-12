import statistics
pop1 = [19, 25, 31, 52, 49, 34, 59, 47, 17, 51]
pop2 = [24, 27, 36, 53, 55, 34, 66, 51, 20, 55]


def get_differences(p1: list[int], p2: list[int]) -> list[int]:
    diff = []
    i = 0
    while i < len(pop1):
        temp = p1[i] - p2[i]
        diff.append(temp)
        i += 1
    return diff


d = get_differences(pop1, pop2)
# print(d)

y1_y2 = sum(d) / len(d)
print(y1_y2)
sd_d = statistics.stdev(d)
print(sd_d)


