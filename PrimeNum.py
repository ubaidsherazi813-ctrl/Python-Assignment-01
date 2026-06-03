def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True    
n = int (input("Enter any number: "))
print(isprime(n))

def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True    

n = int (input("Enter any Number: "))
if isprime(n):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")     
     

    







