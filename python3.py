fav_movie = "Toy Story"
rating = 3
popularity_sc = 72.65
if rating >= 4 and popularity_sc > 80 :
    print("Highly recommended")
elif rating >= 3 and popularity_sc > 70 :
    print( "I recommended it . it is good")
elif rating <= 2 and popularity_sc > 60 :
    print("You should check it out!")
else :
    print("Don't watch it. it is a waste of time")