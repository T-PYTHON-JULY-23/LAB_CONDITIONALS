print("_"*25)
movie = input("Enter the Favorit movie : ")
rating_movie = int(input("Rating of the movie out of 5 : "))

popularity = float(input("Enter the popularity : "))

if (popularity >= 80) or (rating_movie >= 4):
    print("Highly Reommended")
elif (popularity >= 70) or (rating_movie >= 3):
    print("it is good")
elif (popularity >= 60) or (rating_movie >= 2):
    print("You should check it out!")
elif (popularity >= 50) or (rating_movie < 2):
    print("Don't watch it. It is a waste of time")
else:
    print("Don't watch it.")