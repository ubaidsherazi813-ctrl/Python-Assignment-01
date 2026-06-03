# Print Count Digit of Number

n = int (input("Enter any nymbers: "))

count = 0
while n!=0:
    n = n//10
    count+=1
    
print(count)
    
# Print Count Digit of Number Using Function

def count(n):
    count = 0
    while n!=0:
        n = n//10
        count+=1
        
    print(count)

n = int (input("Enter any numbers: "))   
count(n)     
