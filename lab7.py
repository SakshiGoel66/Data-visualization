#  ques1: Hi! I am new to Python numpy Can you generate some real world situations where I can use a 
# numpy array with some source code


import numpy as np
import matplotlib.pyplot as plt
n_steps = 1000
steps = np.random.choice([-1, 1], size=n_steps)
position = np.cumsum(steps)
plt.plot(position)
plt.title("Random Walk")
plt.xlabel("Step")
plt.ylabel("Position")
plt.show()




# ques2: Hil Let's create a real-life example involving weather data Use NumPy to analyze temperature data
#  for a week, perform slicing, indexing, shaping, and reshaping operations, and calculate various statistics

import numpy as np

temperature_data = np.array([
    [22.5, 24.0],
    [21.0, 23.5],
    [19.5, 25.0],
    [22.0, 26.0],
    [23.0, 24.5],
    [24.0, 25.5],
    [25.5, 26.5]
])

print("Temperature Data (7 days x 2 cities):")
print(temperature_data)
average_temp_city_a = np.mean(temperature_data[:, 0])
average_temp_city_b = np.mean(temperature_data[:, 1])
max_temp_city_a = np.max(temperature_data[:, 0])
min_temp_city_a = np.min(temperature_data[:, 0])
max_temp_city_b = np.max(temperature_data[:, 1])
min_temp_city_b = np.min(temperature_data[:, 1])
print("\nStatistics:")
print(f"City A - Average Temperature: {average_temp_city_a:.2f} °C")
print(f"City A - Highest Temperature: {max_temp_city_a:.2f} °C")
print(f"City A - Lowest Temperature: {min_temp_city_a:.2f} °C")
print(f"City B - Average Temperature: {average_temp_city_b:.2f} °C")
print(f"City B - Highest Temperature: {max_temp_city_b:.2f} °C")
print(f"City B - Lowest Temperature: {min_temp_city_b:.2f} °C")

day_3_temps = temperature_data[2, :]
print("\nTemperatures on Day 3:")
print(f"City A: {day_3_temps[0]} °C")
print(f"City B: {day_3_temps[1]} °C")

city_b_temps = temperature_data[:, 1]
print("\nTemperatures for City B over the week:")
print(city_b_temps)

reshaped_data = temperature_data.T
print("\nReshaped Data (Cities x Days):")
print(reshaped_data)
