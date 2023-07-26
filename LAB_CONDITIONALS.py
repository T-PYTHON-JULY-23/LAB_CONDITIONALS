


movie = "La Casa De Papel"
rate = 3
popularity=72.65

if rate >= 4 or popularity > 80 :
    print ("Highly recommended")

elif rate >= 3 or popularity > 70 :
    print ("I recommended it . It is good")

elif rate >= 2 or popularity > 60 :
    print ("You should check it out!")

else :
    print("Don't watch it. It is a waste of time") 



print("*"*100)
### Bonus

name = input ("your Name : ")
email = input ("your Email : ")

if len(name) > 2   and  email.endswith("@gmail.com") :
    print (f" welcome {name} you registered with the email {email} ")

elif len(name) > 2 :
     print (" the email is not valid , please provide a valid email  ")

elif email.endswith("@gmail.com"):
    print ("the name length must be more than 2 characters, please provide a valid name.")
               
else :
    print ("the name and email is not valid , please provide a valid name and email.")

    





