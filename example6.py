# Ask the user to enter the base and height of a rectangle, and calculate and display its area and perimeter on the screen

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Calcular el área y el perímetro del rectángulo
area = base * altura
perimetro = 2 * (base + altura)

# Mostrar los resultados por pantalla
print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")
