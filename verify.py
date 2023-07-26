while True:
    name = input("Please Enter Your Name : ")
    email = input("Please Enter Your Email : ")

    if len(name) > 2:
        if not email.endswith('@gmail.com'):
            print(f"Wellcom {name}, you registred with the email {email}")
            break
        else:
            print("the email is not valid , please provide a valid email")
    else:
        print("the name length must be more than 2 characters, please provide a valid name.")