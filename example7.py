# Build an algorithm that simulates a menu of options to perform the four basic arithmetic operations (addition, subtraction, multiplication and division) with two integer numerical values. The user must also specify the operation with the first character of the operation they wish to perform: 'S' or 's' for addition, 'R' or 'r' for subtraction, 'M' or 'm' for multiplication and 'D' or 'd' for division.


num1 = int(input("Add the first number: "))
num2 = int(input("Add the second number: "))

# show the menu options and ask for the operation
print("Operations menu:")
print("A/a: Add")
print("S/s: Subtract")
print("M/m: Multiply")
print("D/d: Divide")
option = input("Add the letter of the desired operation: ").upper()

# Realizar la operación según la opción seleccionada
if option == 'A':
    result = num1 + num2
    operation = "add"
elif option == 'S':
    result = num1 - num2
    operation = "subtract"
elif option == 'M':
    result = num1 * num2
    operation = "multiply"
elif option == 'D':
    result = num1 / num2 if num2 != 0 else "Error: Not divisible"
    operation = "divide"
else:
    result = "Error: Operación no válida"
# Realizar la operación según la opción seleccionada

print(f"El resultado de la {operation} es: {result}")