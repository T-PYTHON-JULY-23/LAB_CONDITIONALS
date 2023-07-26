
name = input("Please Enter Your name: ")
email = input("Please Enter Your Email: ")

if not len(name) > 2:
      print("the name length must be more than 2 characters, please provide a valid name.")

elif len(name) > 2 and email.endswith("@gmail.com"):
       print(f" welcome {name}, you registered with the email {email}!")
else:
        print("the email is not valid , please provide a valid email .")


 
             
