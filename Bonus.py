### write a program that asks the user to provide his name and his email using input , then do the following:
name = input("Enter your name:")
email = input("Enter your email:")
#- Check that the name length is more than 2 characters.
if len(set(name)) > 2 :
    print("")
#- Check that the email is valid (using string operations and coditionals)
elif "@" in email:
    print("valid")
#- You only accept @gmail emails . 
elif "@gmail" in email:
    print("Valid name")
#- if the email is valid, display a welcome message to the user . for example :
elif "@gmail.com" in email:
    print(f"welcome {name}, you registered with the {email}!")
#- if the email or name is not valid, display the message : 
if "@gmail" not in email:
    print("the email is not valid , please provide a valid email")

if len(set(name)) <= 2 :
    print("the name length must be more than 2 characters, please provide a valid name.")
