(n, m) = list(map(int, input("Entrez le nombre d'amis et le nombre de jours consécutifs utilisables.").split())) # 2 variables
jours = list(map(int, input("Entrez chaque jour où un ami est présent à Manhattan.").split())) # list of numbers
jours.sort() # list sorted

difference = []  # list which contains the difference between i and i+1
for i in range(0, n-1):
    following_day = jours[i + 1]
    difference.insert(len(difference), abs(jours[i] - following_day))
    print("d", difference)

nb_points = []
counter = 0
iterater = 0

while iterater < n:  # as long as counter is inferior to the number of days OR iterater is inferior to the number of friends
    for l in range(iterater, n-1):  # execute a for loop that will add the difference starting from the iterater to the number of friends
        forward_check = counter + difference[l]
        if forward_check < m:
            counter += difference[l]
            print("c", counter)
            print("d", difference[l])
        elif forward_check >= m:
            break

    iterater += 1  # add one to the iterater
    nb_points.insert(0, counter)  # insert the counter in nb_points
    counter = 0

print(nb_points)


#def manhattan_maboul0(m, jours, n):



#manhattan_maboul0(m, jours, n)







# n = nombre d'amis
# m = nombre de jours consécutifs utilisables
# jours = jour où les amis sont présents (1, 2, 3, 17, 53...)

#étape 1 : mettre en ordre les chiffres
#étape 2 : mesurer la valeur absolue entre chaque nombre avec une suite
#créer un dictionnaire avec position: et nombre d'amis sur la position:
# ajouter +1 à chaque fois qu'un
#une fois qu'on a l'écart entre chauqe nombre...
#objectif : maximiser le nombre de points
# find the position of each point
# we need to fit the highest number of points within a period of n
# if you have the difference between each number, you have to add up


# difference[n] and difference[n+1] : while result <= number of days -> put the number of points in a list
# make a counter and start back at [n+1]

