while True:
    
    print("Hello, Welcome! \nEnter your credentials to login")
    userName = input("Email address: ")
    Password = input("Password: ")
        
    if userName !='' and Password != '':
        if "@" and ".com" in userName or ".ac.ke" in userName:
            if "gmail" or "yahoo" or "mail" or ".ac.ke" in userName:
                if len(Password) >= 8:
                    print("Login Successful! You can access our services.")
                    break
     
                else:
                    print("Invalid Password. Password should have at least 8 characters")
            else:
                print("Invalid Email address.\nPlease try again.")
        else:
            print("Invalid Email address.\nPlease try again.")
    else:
          print("Enter all fields")