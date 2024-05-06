# implement a recursive method that allows you to know the number of digits a number has. For example add 100 result 3 digit

def contar_digitos(num):
    # Caso base: si el número es menor que 10, tiene un solo dígito
    if num < 10:
        return 1
    # Caso recursivo: dividir el número por 10 para eliminar un dígito y llamar de nuevo a la función
    else:
        return 1 + contar_digitos(num / 10)



numero = int(input("Ingrese un número natural: "))

if numero < 0:
    print("Error: El número debe ser positivo.")
else:
    cantidad_digitos = contar_digitos(numero)
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")

