#Calculator Using Arithmetic Operator

def calculator(a,b,ope):
    if ope == '+':
        print(a+b)
    elif ope == '-':
        print(a-b)
    elif ope == '*':
        print(a*b) 
    elif ope == '/':
        print(a/b)
    else:
        print("Invalid Ope")             

a = int (input("Enter first Number: "))
b = int (input("Enter second Number: "))
ope = (input("Enter any operation(+,-,*,/): "))
calculator(a,b,ope)  

# Calculator Using Arithmetic Operator 2nd Method

def calculator(a,ope,b):
    if ope == '+':
        print(a+b)
    elif ope == '-':
        print(a-b)
    elif ope == '*':
        print(a*b) 
    elif ope == '/':
        print(int(a/b))
    else:
        print("Invalid Ope")             

a = int (input("Enter first Number: "))
ope = (input("Enter any operation(+,-,*,/): "))
b = int (input("Enter second Number: "))

calculator(a,ope,b,) 
