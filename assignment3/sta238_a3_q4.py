early = [68, 138, 75, 186, 68, 217, 93, 90,
         71, 154, 166, 130, 72, 81, 76, 129]
evening = [299, 367, 331, 257, 260, 269, 252, 200,
           296, 204, 190, 240, 350, 256, 282, 320]
late_night = [216, 175, 274, 171, 187, 213, 221, 139,
              226, 128, 236, 128, 217, 196, 201, 161]

y_i_dot = sum(early) + sum(evening) + sum(late_night)
print(y_i_dot)

def get_sum_squared(i: list[list[int]]) -> int:
    ss = 0
    for t_i in i:
        ss_j = 0
        for j in t_i:
            ss_j += (j**2)
        ss += ss_j
    return ss

# yij_squared = get_sum_squared([early, evening, late_night])
# print(yij_squared)

def get_ss(data: list[int]) -> int:
    ss = 0
    for num in data:
        ss += num**2
    return ss

ss_early = get_ss(early)
ss_evening = get_ss(evening)
ss_late = get_ss(late_night)
print(ss_early + ss_evening + ss_late)

all_data = early+evening+late_night
print(all_data)
print(len(all_data))
print(sum(all_data))

yij_squared = get_ss(all_data)
print(yij_squared)
