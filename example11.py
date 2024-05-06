# Enter two numbers and implement a recursive method that allows you to perform a division using subtraction.

def division_por_restas(dividendo, divisor):
    # Caso base: cuando el dividendo es menor que el divisor, el cociente es 0
    if dividendo < divisor:
        return 0
    # Caso recursivo: restar el divisor del dividendo hasta que sea menor que el divisor
    else:
        return 1 + division_por_restas(dividendo - divisor, divisor)
dividendo = int(input("Ingrese el dividendo (número mayor): "))
divisor = int(input("Ingrese el divisor (número menor): "))

# Validar que el divisor no sea 0
if divisor == 0:
    print("Error: No se puede dividir por 0.")
else:
    # Calcular y mostrar el cociente usando la función recursiva
    cociente = division_por_restas(dividendo, divisor)
    print(f"El cociente de la división es: {cociente}")