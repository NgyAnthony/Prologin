from contextlib import suppress

(n, m) = list(map(int, input("Entrez le nombre d'amis et le nombre de jours consécutifs utilisables.").split()))
jours = list(map(int, input("Entrez chaque jour où un ami est présent à Manhattan.").split()))
if len(jours) > n:
    print("Contrainte: le nombre de journées visitées est supérieur au nombre d'amis.")
    quit()
liste_p_a = [None] * n


def manhattan_maboul0(m, jours, n):
    for i in range(0, n):
        nb_amis = jours.count(jours[i])
        jours_amis = {"jours": jours[i], "nb_amis": nb_amis}
        for x in range(0, n):
            if type(liste_p_a[x]) != dict:
                break

            elif liste_p_a[x].get("jours") == jours_amis.get("jours"):
                del liste_p_a[x]
                liste_p_a.insert(0, None)
        liste_p_a[i] = jours_amis

    while None in liste_p_a:
        liste_p_a.remove(None)

print(liste_p_a)

    # If I make a dictionnary and insert in the "jours" a list of the used positions associated with the difference
    # and then
    #FORWARD Checking
    # calculate the difference between all the points
    # return the difference between all the points in a list
    # check if adding the difference to the total will make m < total

    #ADDING to a list
    # repeat this process x times
        # start at liste_p_a[x]:

#I have a list of Position associated with the number of friends on this position

#Tant que la différence est inférieure au nombre de jours
    #Ajouter la position à listejours
    #Rajouter +1 à l'iteration
#Recommencer la même boucle avec iterater




manhattan_maboul0(m, jours, n)

#I have two variables, n which is the number of friends and m which is the number of days I'll use.
#I also have a list of days where each friend will be at Manhattan.
#What I want is to maximize the number of friends I'll be able to see in a period of time m.

#Make a dictionnary list with the position of each point and the number of points on the position.
#Get the difference between each position.
#The chosen period must be dependant on the number of points.

#Add up the difference of position until the difference gets than the number of days
#Add the number of points of the positions to a sum
#Add this sum to a list
#Once this is done, repeat the process but on the next position
#Return the list of sum and take the highest one.




#for each day corresponding to the key in jours_amis, add +1 to nb_amis