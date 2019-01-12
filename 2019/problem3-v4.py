def manhattan_maboul0(m, jours, n):
    """
    Check paramètres illégaux.
    """
    if n <= 1 or n >= 100:
        print("Erreur : domaine de validité non respecté(nombre d'amis).")
        quit()
    if m <= 1 or m >= 36:
        print("Erreur : domaine de validité non respecté(jours consécutifs).")
        quit()
    for p in range(len(jours) - 1):
        if jours[p] < 1 or jours[p] >= 1000000:
            print("Erreur : domaine de validité non respecté(journée sélectionnée).")
            quit()
        if type(jours[p]) != int:
            print("Erreur : n'utilisez que des nombres valides.")
            quit()

    if type(n) != int or type(m) != int:
        print("Erreur : 'int' uniquement autorisés.")
        quit()

    if len(jours) > n:
        print("Erreur : trop de jours attribués.")
        quit()
    if len(jours) < n:
        print("Erreur : pas assez de jours attribués.")
        quit()

    """
    Cette partie du code créer le quadrillage en indiquant le jour et le nombre de personnes sur ce jour.
    Chaque jour où il n'y a personne est remplacé par un type(None)
    """
    abscisse = [None] * (max(jours) +1)# Créer le quadrillage jusqu'a jour maximal.
    for i in range(0, len(jours)): # Itérer une boucle qui va de 0 jusqu'a la longueur de la liste où chaque jour un ami est présent
        a = type(abscisse[jours[i]])
        if a == type(None): # Si le type de la liste d'abscisse à la position du jour n'est pas égal à None
            step = {"jours": jours[i], 'nb_on_pos': 1} # Rajouter un dict avec le jour concerné et un nombre d'ami égal à 1
            abscisse[jours[i]] = step

        elif type(abscisse[jours[i]]) != type(None) and jours[i] == abscisse[jours[i]].get('jours'): # Si le type n'est pas None ET à le jour relevé = au jour déjà présent
            adder = abscisse[jours[i]].get('nb_on_pos')
            adder += 1  # Rajouter 1 au nombre d'ami sur la position
            abscisse[jours[i]].update({"jours": jours[i], 'nb_on_pos': adder}) #Mettre à jour le nombre de personnes sur la position

    """
    Cette partie du code va itérer la longueur de abscisse. Si il y a un type différent de None, le jour va être rajouté dans une liste
    l'algo va ajouter +1 à un compteur jusqu'à ce qu'il trouve type différent de None. Une fois trouvé, il va rajouter le jour dans la liste.
    Si le compteur est plus grand que le nombre de jours, il faut arrêter.

    Une boucle fait recommencer cette algorithme en faisant commencer le compteur à chaque jour.
    Une fois ça fait, on aura une liste de combinaison de jours valides.
    Il nous suffit alors d'ajouter la position de chaque combinaison et de prendre la plus grande.
    """
    days_wo_duplicate = list(set(jours))
    days_wo_duplicate.sort()
    list_of_combination = []
    for l in range(len(days_wo_duplicate)):
        counted_days = 0
        step2 = days_wo_duplicate[l]
        combination = []
        while counted_days < m:
            if type(abscisse[step2]) != type(None):
                combination.append(step2)
            counted_days += 1
            if days_wo_duplicate[len(days_wo_duplicate) - 1] == step2:
                break
            step2 += 1
        list_of_combination.append(combination)


    """
    Liste_de_combinaisons qui nous donne toutes les combinaisons valides.
    Cette fonction calcule la somme de chaque combinaison et retourne la valeur maximale.
    """
    sums = []
    for x in range(len(list_of_combination)):
        current_sum = 0
        for o in range(len(list_of_combination[x])):
            for z in range(len(abscisse)):
                if type(abscisse[z]) != type(None) and list_of_combination[x][o] == abscisse[z].get('jours'):
                    current_sum += abscisse[z].get('nb_on_pos')
        sums.append(current_sum)
    print(max(sums))

(n, m) = list(map(int, input().split()))
jours = list(map(int, input().split()))

manhattan_maboul0(m, jours, n)


#todo ne respecte pas du tout les contraites de performance.
#todo cleanup avec def et class