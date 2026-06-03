# Print Reverse Digit Number

n = int (input("Enter any numbers: "))

while n!=0:
    digit = n%10  
    n = n//10    
    print(digit,end="")

# Print Reverse Digit Number Using Function   

def rev(n):
    while n!=0:
        digit = n%10
        n = n//10
        print(digit,end="")  

n = int (input("\nEnter any numbers: "))
rev(n)      


   
          
