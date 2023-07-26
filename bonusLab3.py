#bonus lab3

userName = input("enter your name: ")
email = input("enter your email: ")

if len(userName)> 2:
    if email.count(" ") == 0 and email.endswith("@gmail.com"):
     print("welcome",userName, "you registered with the email", email)
    else:
     print(" please provide a valid email")
else: 
    print("the name length must be more than 2 characters, please provide a valid name.")

