print("welcome: ")


name = input("Enter your name :")
email = input("Enter your email :")

if (len(name) > 2) and email.endswith("@gmail.com"):
      print(f"welcome {name}, you registered with the {email} !")

elif len(name) <= 2:
      print("the name length must be more than 2 characters, please provide a valid name.")

elif email.endswith != ("@gmail.com"):
      print("the email is not valid , please provide a valid email .")









