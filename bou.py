name = input("what u name ? ")
EmailUser =input("input u email: ")


if len(name) > 2:
    if "@gmail" in EmailUser :
     print(f"welcome {name}, you registered with the email {EmailUser} !")

    else:
     print(" the email is not valid , please provide a valid email .")

else:
    print("the name length must be more than 2 characters, please provide a valid name.")