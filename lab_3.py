
movie_name = input("enter the movie name : ")
movie_rating = int(input("enter your rating out of 5: "))
popularity_score = float(input("enter popularity_score: "))

if movie_rating >= 4 and popularity_score > 80:
    print(" Highly recommended")
elif movie_rating >= 3 and popularity_score > 70:
    print(" I recommended it")
elif movie_rating >= 2 and popularity_score > 60:
    print(" You should check it out!")
else:
    print("Don't watch it. It is a waste of time")
