
# Build an algorithm that simulates a menu of options to perform the four basic arithmetic operations (addition, subtraction, multiplication and division) with two integer numerical values. The user must also specify the operation with the first character of the operation they wish to perform: 'S' or 's' for addition, 'R' or 'r' for subtraction, 'M' or 'm' for multiplication and 'D' or 'd' for division.

num1 = int(input("add the first number "))
num2 = int(input("add the second number "))

print("Operations Menu")
print("A/a for adding")
print("S/s for subtracting")
option = input("add the operation you want ").upper()

if option == "A":
    result = num1 + num2
    operation = "addition"
elif option == "S":
    result = num1 - num2
    operation = "subtraction"
else:
    operation = "error"
    result = "Error"

print(f"The result of the {operation} is {result}")
