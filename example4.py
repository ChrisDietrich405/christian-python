# Write an algorithm that determines if a number is between 0 and 10, if it is between 0 and 10 the number will be requested again until the number is correct.

while True:
    try:
        print("add a number")
        number = int(input())
        if 0 <= number <= 10:
            print("great job")
            break
        else:
            print("you fucked up, try again")
    except ValueError:
        print("add a new number")

            
 




















# while True:
#     try:
#         number = float(input("input a number between 0 and 10: "))
#         if 0 <= number <= 10:
#             print("the number is correct.")
#             break  # Sale del bucle si la nota es válida
#         else:
#             print("La nota debe estar entre 0 y 10. Inténtelo nuevamente.")
#     except ValueError:
#         print("Por favor, ingrese un número válido.")
