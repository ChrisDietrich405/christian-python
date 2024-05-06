def count_digits(num):
    if num < 10:
        return 1
    else:
        return 1 + count_digits(num / 10) 
    
number = int(input("ADD A NUMBER"))

if number < 0:
    print("add a positive number")
else: 
    number_of_digits = count_digits(number)
    print(f"the number {number} has this many digits {number_of_digits}")

