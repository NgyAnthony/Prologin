for r in range(0, len(liste_p_a) - 1):
    if iterater < len(liste_p_a) - 1:
        difference = abs(liste_p_a[r] - liste_p_a[r + 1])
        iterater += 1
    difference_jours_amis = {"difference": difference, "jours": liste_jours, "nb_amis": nb_amis}

for r in range(0, len(liste_p_a) - 1):
    forward_check = abs(liste_p_a[r] - liste_p_a[r + 1])
    while forward_check < m:
        difference = abs(liste_p_a[r] - liste_p_a[r + 1])


    l = 0
    counter = 0
    for i in range(0, n):
        forward_count = 0
        while forward_count < m:
            difference = abs(liste_p_a[l].get("jours") - liste_p_a[l+1].get("jours"))
            forward_count = counter + abs(liste_p_a[l+1].get("jours") - liste_p_a[l+2].get("jours"))
            counter += difference
            l += 1
            print("c", counter)
            print(difference)



    difference_liste = []
    for l in range(0, n-1):
        difference = abs(liste_p_a[l].get("jours") - liste_p_a[l+1].get("jours"))
        difference_liste.insert(len(difference_liste), difference)
        print(difference_liste)

        for r in range(0, len(liste_p_a)):
            if jours_amis.get(jours) == liste_p_a[r].get(jours):
                liste_p_a[r].remove()
                n -= 1

    difference_list = []
    for i in range(0, n - 1):
        difference = abs(jours[i] - jours[i + 1])
        difference_list.insert(len(difference_list), difference)

for r in range(0, days_wo_duplicates):
    day_nbfriends_diff = {"jours": days_wo_duplicates[r], "nb_amis": nb_amis, "difference": difference}

difference_list = []

for i in range(0, len(days_wo_duplicates) - 1):
    difference = abs(days_wo_duplicates[i] - days_wo_duplicates[i + 1])
    difference_list.insert(len(difference_list), difference)

print("Liste des différences entre les jours", difference_list)

forward_checking = 0
forward_checking += difference
if forward_checking > m:
    continue
elif forward_checking < m:

    # HERE : Delete all the data from the last difference_sum[s-1]
    # recall diff, friends and s to 0
    # Invoke getFinalList

    def getFinalList(days_list_added, difference_sum, friends_sum, days_wo_duplicate):
        for z in range(0, len()):
    # or just get the highest number of days...

    # To get the final list, create a dictionary with every variable

    print("difference_sum", difference_sum)
    print("friends_sum", friends_sum)
    print("s", s)
    print("days_list", days_list_added)









 for f in range(0, len(all_items_list) - 1): # For loop repeated to the length of all the data collected before
        difference_sum = 0
        friends_sum = 0
        while difference_sum < m: # As long as the sum is inferior to the number of days
            s += 1 # Add +1 to "s" which will be used as a counter
            difference_sum = difference_sum + all_items_list[s].get("difference") + all_items_list[s+1].get("difference") # Add the differences between "s" and "s+1"
            days_list_added = all_items_list[s].get("jours") + all_items_list[s+1].get("jours") # Add the list of "s" and "s+1"
            friends_sum += all_items_list[s].get("nb_amis") + all_items_list[s+1].get("nb_amis") # Add the number of friends

            cross_duplicate_days = list(set(days_list_added))
            is_there_duplicates = abs(len(cross_duplicate_days) - len(days_list_added)) # Remove every duplicate in the list of days

            if is_there_duplicates > 0: # If duplicates are detected
                for x, p in zip(range(0, len(cross_duplicate_days)), range(0, len(all_items_list))):
                    if cross_duplicate_days[x] == individual_list[p]: # Identify the numbers which are duplicated ; look if one of them corresponds to the individual list.
                        friends_sum -= individual_list[p].get('nb_amis') # Remove the number of friends once

            highest_friend.insert(0, friends_sum)

    print("Nombre d'amis que l'on peut voir en %i jours : %i" % (m, max(highest_friend)))

final_friends_amount = []
    n = 0
    for f in range(0, len(all_items_list)):
        s = n
        difference_sum = 0
        total_friends = 0
        all_positions = []

        while difference_sum < m:
            difference_sum += all_items_list[s].get('difference')
            s += 1

        if len(all_items_list) > n:
            n += 1

        for r in range(f, n):
            total_friends += all_items_list[r].get('nb_amis')
            all_positions += (list(set(all_items_list[r].get('jours'))))

        cross_duplicate_days = list(set(all_positions))
        is_there_duplicates = abs(len(cross_duplicate_days) - len(all_positions))  # Check if there are duplicates
        if is_there_duplicates > 0:
            for x, p in zip(range(0, len(cross_duplicate_days)), range(0, len(individual_list))):
                if cross_duplicate_days[x] == individual_list[p].get("jours"):
                    remover = individual_list[p].get("nb_amis")
                    total_friends -= remover
        final_friends_amount.insert(0, total_friends)
        print(total_friends)

for x, p in zip(range(0, len(cross_duplicate_days)),
                range(0, len(individual_list))):  # TODO : Make a valid for loop that removes duplicates
    if cross_duplicate_days[x] == individual_list[p].get("jours"):
        remover = individual_list[p].get("nb_amis")
        total_friends -= remover
final_friends_amount.insert(0, total_friends)


k = all_items_list[len(all_items_list) -1].get('jours')  # Identifies if the previous key is the last key in the list
        p = (list(set(all_items_list[s + 1].get('jours'))))  # If it is, don't backtrack

        if k != p: