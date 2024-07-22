#ques1: wap to handle ZeroDivisionError exception

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Error: You cannot divide a number by zero.")

#ques2: 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

try:
    user_input = input("Enter an integer: ")
    user_int = int(user_input)
    print(f"You entered the integer: {user_int}")
except ValueError:
    print("Error: The input is not a valid integer.")


#ques3: 3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    filename = input("Enter the filename to open: ")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")


#ques4: Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical

try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = float(num1) + float(num2)
    print(f"The sum of the numbers is: {result}")
except ValueError:
    print("Error: Both inputs must be numbers.")
