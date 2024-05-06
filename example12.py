def division_by_subtraction(dividend, divisor): 
    if dividend < divisor:
        return 0

    else:
        return 1 + division_by_subtraction(dividend - divisor, divisor)

dividend = int(input("add a big number"))    
divisor = int(input("add a little number"))    

if(divisor == 0):
    print("big problems")
else: 
    quotient = division_by_subtraction(dividend, divisor)
    print(f"the quotient is {quotient}")