#  Implement a program that, given two numbers determines which is the largest and show it on the screen

# class LargestNumber: 
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def twoNumbersFunction(self):
#         if self.num1 > self.num2:
#             print(self.num1)
#         else:
#             print(self.num2)

# LargestNumberObj = LargestNumber(2,5)

# print(LargestNumberObj.twoNumbersFunction())
     
# print("add first number")
# num1 = int(input())
# print("add second number")
# num2 = int(input())

# if num1 == num2:
#     print("they are the same")
# else:
#     if num1 > num2: 
#         print(f"the largest number is", num1)
#     else:   
#         print(f"the largest number is", num2)


# Create a program that, given a number, determines if it is even or odd.

# number = int(input("add a number"))

# if number % 2 == 0:
#     print(f"the number {number} is even")
# else:
#     print(f"the number {number} is odd")

# Write a program that asks for a sentence and displays it all in uppercase and then all in lowercase.

# Write a program that asks for a word that validates whether its first letter is an 'A'

# Make a program that allows you to enter 3 numbers. Must show average grade

# numUno = int(input("nota 1: ")) 
# numDos = int(input("nota 2: ")) 
# numTres = int(input("nota 3: ")) 

# prom = numUno + numDos + numTres / 3

# print("Notas: ",numUno, numDos, numTres, "Promedio: ",prom)

# cadena_formato = f"Notas:{numUno:03}{numDos:03}{numTres:03} ==> Promedio:{prom:8.02}"
# print (cadena_formato)

# Write a program that asks the user for a word and displays it on the screen 10 times.

# wordInput = input("add a word")
# print(wordInput)

# result = input("add a word")

# for result in range(10):
#    print(result)

# my_string = input("add a word ")
# number = 10
# result = my_string * number
# print(result)


#  Write a program that asks the user for a word, stores it in a list and displays on the screen the number of times each vowel appears


# word = input("add a word\n")

# word = word.lower()

# vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}

# for letter in word:
#     if letter in vowels:
#         vowels[letter] += 1

# for vowels, count in vowels.items():
#     print(f"the {vowels} appear {count} many times")







# for letra in palabra:

#     if letra in vocales:
#         vocales[letra] += 1

# for vocal, conteo in vocales.items():
#     print(f"La vocal {vocal} aparece {conteo} veces en la palabra.")



# my_dict = {'a': 1, 'b': 2, 'c': 3}

# # Using items() to loop through key-value pairs
# for key, value in my_dict.items():
#     print(key, "->", value)



# Store 10 numbers in a list and display the smallest and largest on the screen.

# num = [50, 75, 46, 22, 80, 65, 8] 

# min = num[0]
# max = num[0]  

# for numElement in num:
#     if numElement < min:
#         min = numElement
#     elif numElement > max:
#         max = numElement

# print("El maximo es "+str(max))
# print("El minimo es "+str(min))


# lists - arrays, tuples - immutable objects, 

# Sets (set): An unordered collection of unique elements. Useful for operations like union, intersection, and difference. Example: {1, 2, 3, 4}.
    
# dicts - objects

# a set can be an object 

# { 1, 3, 4, 5 } this is an object and it is also a set
# it seems easy

# dominion Model 

# Define two sets
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}

# # Perform a union of set_a and set_b
# union_newSet = set_a | set_b
# print(union_newSet)
# union_set = set_a.union(set_b)

# # Display the result
# print("Union using method:", union_set)  # Output: {1, 2, 3, 4, 5}

# # Define two sets
# set_x = {'apple', 'banana', 'cherry'}
# set_y = {'banana', 'date', 'elderberry'}

# # Perform a union of set_x and set_y using the | operator
# union_set = set_x | set_y

# # Display the result
# print("Union using operator:", union_set) 

# Exercise 1. Write an algorithm that requests two integers by keyboard and calculates the sum of the two. The algorithm should then display the result of the sum

print("add two numbers ")
num1 = int(input())
num2 = int(input())

print(num1 + num2)
















# def addTwoNumbers(num1, num2):
#     request = input(f"add two numbers ${num1} ${num2}" ) 
#     print(request)

# addTwoNumbers(firstNumber, secondNumber)


