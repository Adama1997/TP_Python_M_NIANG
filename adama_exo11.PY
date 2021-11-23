import random
n = random.randint(1,100)
nbr_tenter=48
i=1
while (nbr_tenter > 0):
    nbr_tenter-=1
    var=int(input("entrer un nombre: "))
    if var < n:
        print("c'est petit hein......")
    elif var > n:
        print("plus grand quand meme.... ")
    else:
        print("t'as gagné wei.......")
