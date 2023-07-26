#lab3


movie = "titanic"
rating = int(input("inter the rate of the movie: "))
PopularityScore = float(72.65)

if rating >= 4 and PopularityScore>=80:
    print(" highly recomended ")
elif rating >= 3 and PopularityScore>=70:
    print("I recommended it . It is good")  
elif rating >=2 and PopularityScore>=60:
    print("You should check it out!")
else:
    rating <=2 and PopularityScore<=50
    print("Don't watch it. It is a waste of time")