def AuthUsername():
    
    attempts = 3
    
    flag = False
    while flag != True:
        
        while attempts != 0: 
            username = input("Enter the username: ")
            if username == "akshay":
                flag = True
                break
            else:
                print("Invalid username")
                attempts = attempts - 1
                print("Attempts left: ", attempts)
        if attempts == 0:
                print("Your account is locked. Please contact Administrator.")
                flag = False
                break
    return flag
                
def AuthPassword():
    from getpass import getpass
    
    flag = False
    attempts = 3
    while flag != True:
        while attempts !=0:
            password = getpass("Enter the password: ") 
            if password == "akshay":
                flag = True
                break
            else:
                print("Invalid Password")
                attempts = attempts - 1
                print("Attempts left: ", attempts)
        if attempts == 0:
            print("Your account is locked. Please contact Administrator.")
            flag = False
            break
    return flag
    
    