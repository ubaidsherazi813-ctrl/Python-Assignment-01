def guess_num():
    secret_num = 26

    while True:
        guess = int(input("Enter any Number: "))
        if secret_num>guess:
            print("Two High : Try again")
        elif secret_num<guess:
            print("Two Low : Try again") 
        else:
            print("Correct")
            break    
        

guess_num()               



