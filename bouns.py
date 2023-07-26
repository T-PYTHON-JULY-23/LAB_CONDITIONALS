name =input("inter your name :")
email= input("inter your email:")
if len(name)<=2:
    print(f"the name length must be more than 2 characters, please provide a valid name.")

elif email.index("@gmail") :
    print(f"welcome {name}, you registered with the email {email} !")
else:
    print(" the email is not valid , please provide a valid email .")
  