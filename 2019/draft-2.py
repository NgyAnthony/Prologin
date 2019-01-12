(n, m) = list(map(int, "5 2".split())) # Input number of friends and days
jours = list(map(int, "1 1 1 1 1".split())) # Input days where friends are present
jours.sort() # Sort days when friends are in Manhattan
days_wo_duplicates = list(set(jours)) # Remove duplicates
days_wo_duplicates.sort() # Sort the new list
all_items_list = [None] * len(days_wo_duplicates)  # Create slots for each position.
individual_list = [None] * len(days_wo_duplicates)  # Create slots for each position BUT the "jours" is not a list but individual days.
final_list = [None] * len(days_wo_duplicates)


def getAllElements(jours, days_wo_duplicates):
    for i in range(0, len(days_wo_duplicates) - 1): # Create a for loop to assign each value to a dict inside a list
        difference = abs(days_wo_duplicates[i] - days_wo_duplicates[i + 1]) # Calculate the difference between each position
        nb_amis = 0 # Initiate number of friends to 0

        for l in range(0, len(jours)): # Repeat this loop len(jours) times to calculate the number of friends in a position
            if jours[l] == days_wo_duplicates[i]:
                nb_amis += 1 # Add "1" to the number of friends every time an unfiltered(no set()) day in "jours" is detected
            if jours[l] == days_wo_duplicates[i+1]:
                nb_amis += 1 # Same thing but for the number after

        day_nbfriends_diff = {"jours": [days_wo_duplicates[i], days_wo_duplicates[i+1]], "nb_amis": nb_amis, "difference": difference}
        all_items_list[i] = day_nbfriends_diff # Create a dict which returns the difference between two days, their position, and the number of friends on it.


def getIndividualElements(jours):
    for r in range(0, len(days_wo_duplicates)):
        nb_amis = 0  # Initiate number of friends to 0

        for l in range(0, len(jours)):  # Repeat this loop len(jours) times to calculate the number of friends in a position
            if jours[l] == days_wo_duplicates[r]:
                nb_amis += 1  # Add "1" to the number of friends every time an unfiltered(no set()) day in "jours" is detected

        day_nbfriends_diff = {"jours": days_wo_duplicates[r], "nb_amis": nb_amis}
        individual_list[r] = day_nbfriends_diff  # Create a dict which returns the difference between two days, their position, and the number of friends on it.


def removeUnnessecary(all_items_list, individual_list):
    while None in all_items_list:
        all_items_list.remove(None) #If there is a "None" inside the list, remove it to avoid inconsistencies
    while None in individual_list:
        individual_list.remove(None)  # If there is a "None" inside the list, remove it to avoid inconsistencies
    print("ALL", all_items_list)
    print("Individual", individual_list)


def secondFilter(all_items_list, individual_list):
    final_friends_amount = []
    friends_in_individual_list = []
    for f in range(0, len(all_items_list)): # This loop is going to repeat until all positions are tried
        s = f  # Assign s to f to make the calculation of the difference start at the next position
        difference_sum = 0
        total_friends = 0
        all_positions = []

        if len(all_items_list) - 1 == s:
            difference_sum += all_items_list[s].get('difference')
            total_friends += all_items_list[s].get('nb_amis')
            all_positions += (list(set(all_items_list[s].get('jours'))))

        while difference_sum < m and s < len(all_items_list) : # This while loop will add up the difference until m inferior.
            difference_sum += all_items_list[s].get('difference')
            total_friends += all_items_list[s].get('nb_amis')
            all_positions += (list(set(all_items_list[s].get('jours'))))
            s += 1
            a = (list(set(all_items_list[s-1].get('jours')))) # This variable get the last key of the loop

#TODO : make a function for backtracking based on clear conditions :
        # Is difference_sum == m
        # Is the while loop stopping because it's the last one
        # Or are we backtracking
        s -= 1  # Backtrack to the previous position
        b = (list(set(all_items_list[s].get('jours')))) # This variable gets the key of the last in the list
        positions = all_items_list[s].get('jours')
        if m == difference_sum: # This statement doesn't work.
            pass
        elif positions != all_items_list[len(all_items_list)-1].get('jours') or a == b: # Remove the difference of the key which broke the loop above
            difference_sum -= all_items_list[s].get('difference')
            total_friends -= all_items_list[s].get('nb_amis')

        get_last_key_position = (list((set(all_items_list[s].get('jours')))))
        copy = [] + all_positions # I need to make a copy for iteration reasons, dont remove it. Otherwise we're out of range.

        if difference_sum == 0 or difference_sum > m: # This statement nullifies the number of friends if the difference between the two points cannot be reached.
            total_friends = 0
# ISSUE : This removes the position, we don't want to remove the position if we're not backtracking.
        if len(all_positions) != 2:
            for a in range(0, len(get_last_key_position)):  # This for loop removes the last position key
                n = 1
                for t in range(0, len(all_positions)):
                    if get_last_key_position[a] == all_positions[t] and n != 0:
                        copy.remove(get_last_key_position[a])
                        n -= 1
        all_positions = copy

#TODO : make a function to check if there are any duplicates (for example [1,2][2,3]
        cross_duplicate_days = list(set(all_positions))
        is_there_duplicates = abs(len(cross_duplicate_days) - len(all_positions))  # Check if there are duplicates
        duplicate_list = [] + all_positions

        if is_there_duplicates > 0:
            for x in range(0, len(cross_duplicate_days)):
                n = 1
                for z in range(0, len(all_positions)):
                    if cross_duplicate_days[x] == all_positions[z] and n != 0:
                        duplicate_list.remove(cross_duplicate_days[x])
                        n -= 1
            for v in range(0,len(duplicate_list)):
                for u in range(0, len(individual_list)):
                    if duplicate_list[v] == individual_list[u].get('jours'):
                        total_friends -= individual_list[u].get('nb_amis')
        for o in range(0, len(individual_list)):
            friends_in_individual_list.insert(0, individual_list[o].get('nb_amis')) # Insert the number of friends of the individual list

        print(individual_list[0].get('nb_amis'))
        if len(individual_list) == 1:
            friends_in_individual_list.insert(0, individual_list[0].get('nb_amis')) # Insert the number of friends of the individual list
        final_friends_amount.insert(0, total_friends)

#TODO : make a function to print what we need.
    print(friends_in_individual_list)

    if len(friends_in_individual_list) == 0:
        one_day = True
    else:
        one_day = max(final_friends_amount)

    if one_day == True:
        print(max(friends_in_individual_list))
    if len(final_friends_amount) == 0 or max(friends_in_individual_list) > one_day: # If a number in individual list is larger among processed ones, print 'individual'
        print(max(friends_in_individual_list))
    else:
        print(max(final_friends_amount))


def callEveryone():
    getAllElements(jours, days_wo_duplicates)
    getIndividualElements(jours)
    removeUnnessecary(all_items_list, individual_list)
    secondFilter(all_items_list, individual_list)

callEveryone()
