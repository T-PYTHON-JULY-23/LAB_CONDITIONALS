Movie_Name = "Barbie"
print(Movie_Name)
rating = int("3")
score= float("72.65")
print(rating)
print(score)
if  rating>= 4 or score>= 80:
    print("Highly recommended")
elif rating >= 3 or score> 70:
    print("I recommended it . It is good")
elif rating<= 2 or score> 60:
    print("You should check it ot!")
else :
    print("Don't watch it. It is a waste of time")