print("Sign up")
print("-"*20)
name= input("Enter your name: ")
email= input("Enter your email: ")
if not len(name) > 2:
    print('the name length must be more than 2 characters, please provide a valid name.')
if not email.count('@gmail'):
    print('the email is not valid , please provide a valid email')
if len(name) > 2 and email.count('@gmail'):
    print(f'welcome {name}, you registered with the email {email} !')
