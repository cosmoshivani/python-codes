def ask():
    
    while True:
        try:
            n = int(input("Enter a number: "))
        except:
            print("Please try again! \n")
            continue
        else:
            break
        
    print("your number squared is: ")
    print(n)
    
ask()
