
name = input("Please enter your name: ")
email = input("Please enter your email: ")
namelen = len(name)
endofemail = email[-10:]

if (namelen > 2) and (endofemail == "@gmail.com"):
    print(f"welcome {name}, you registered with the email {email} !")
elif namelen <= 2 :
        print("the name length must be more than 2 characters, please provide a valid name.")

elif endofemail != "@gmail.com" :
    print("the email is not valid , please provide a valid email .")


