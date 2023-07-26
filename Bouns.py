user_name = input("Enter your name : ")
email = input("Enter yor email : ")

if len(user_name) > 2:
    if email.endswith("@gmail.com"):
        print("welcome {user_name}, you registered with the email {email} !")
    else:
        print("the email is not valid , please provide a valid email .")
else:
    print("the name length must be more than 2 characters, please provide a valid name.")
