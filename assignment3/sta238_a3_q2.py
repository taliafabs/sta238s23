y_apparent_porosity = [18.8, 18.3, 16.3, 6.9, 17.1, 20.4]
x_mean_pore_diameter = [12.0, 9.7, 7.3, 5.3, 10.9, 16.8]

def get_sum_of_squares(data: list[float]) -> float:
   ss = 0.0
   for i in data:
       ss += i**2
   return ss

sum_xi = sum(x_mean_pore_diameter)
sum_yi = sum(y_apparent_porosity)
print(sum_xi)
print(sum_yi)

ss_x = get_sum_of_squares(x_mean_pore_diameter)
print(ss_x)
ss_y = get_sum_of_squares(y_apparent_porosity)
print(ss_y)

def get_sum_xiyi(x: list[float], y: list[float]) -> float:
    result = 0.0
    for i in range(len(x)):
        result += x[i]*y[i]
    return result

sum_xiyi = get_sum_xiyi(x_mean_pore_diameter, y_apparent_porosity)
print(sum_xiyi)
