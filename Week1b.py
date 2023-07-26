fav_movie="blabla"

movie_rating= int(3)

popularity= float(72.65)


if movie_rating >= 4 and popularity >80:
    print("higly recommended")
elif movie_rating >= 3 and popularity > 70:
    print("I recommended it . It is good")
elif movie_rating <= 2 and popularity> 60:
    print("You should check it out!")
else:
    movie_rating <=2 and popularity <50
    print("Don't watch it. It is a waste of time")