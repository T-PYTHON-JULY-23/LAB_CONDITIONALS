name = input("Please enter your name :")
email = input("Please enter your email :")
print(" ''' \n")

if (len(name) > 2) :
    if (email.endswith("@gmail.com")) :
        print (f"welcome {name}, you registered with the email: {email} !")
    else :
        print("the email is not valid , please provide a valid email .")
else :
    print("the name length must be more than 2 characters, please provide a valid name.")
print (" ''' ")