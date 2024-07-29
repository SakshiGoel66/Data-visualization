 # Convert the below list into numpy array then display tha array 
# input: my_list = [1,2,3,4,5]

import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)

# ===============================================

# Convert the below list into a numpy array then display the 
# array then display the first and last index and then multiply
# each element by 2 and display the result

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print("Array:", my_array)
print("First element:", my_array[0])
print("Last element:", my_array[-1])
doubled_array = my_array * 2
print("Array after doubling each element:")
print(doubled_array)


# ==================================

# write a numpy program to create an array of 10 zeros,10 ones and 10 fives

zeros_array = np.zeros(10)
ones_array = np.ones(10)
fives_array = np.full(10, 5)
print("An array of 10 zeros:")
print(zeros_array)
print("An array of 10 ones:")
print(ones_array)
print("An array of 10 fives:")
print(fives_array)


# ============================================

# write a numpy program to create a 3x3 matrix with values 
# ranging from 2 to 10

matrix = np.arange(2, 11).reshape(3, 3)
print("3x3 matrix with values ranging from 2 to 10:")
print(matrix)
