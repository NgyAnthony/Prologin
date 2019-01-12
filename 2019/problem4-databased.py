list_id = [{"ville": 1, "waiting_time": 5}, {"ville": 2, "waiting_time": 5},
           {"ville": 3, "waiting_time": 10}]

list_trajetv =[{"départ": 1, "arrivée": 2, "tps_trajet": 2}, {"départ": 2, "arrivée": 1, "tps_trajet": 20},
{"départ": 3, "arrivée": 1, "tps_trajet": 5}, {"départ": 2, "arrivée": 3, "tps_trajet": 1}]

list_trajetg =[{"départ": 2, "arrivée": 3, "tps_trajet": 5}]

def bus(list_id, list_trajetv, list_trajetg):
    arrival_list = []
    for x in range(len(list_trajetv)):
        ar_v = list_trajetv[x].get('arrivée')
        arrival_list.append(ar_v)
    for a in range(len(list_trajetg)):
        ar_g = list_trajetg[a].get('arrivée')
        arrival_list.append(ar_g)
    arrival_list = list(set(arrival_list))

    for p in range(len(arrival_list)):
        for i in range()

"""

{"départ": 1, "arrivée": 2, "addup": 7}
{"départ": 1, "arrivée": 3, "addup": 13}

{"départ": 2, "arrivée": 1, "addup": 25}
{"départ": 2, "arrivée": 1, "addup": 21}
{"départ": 2, "arrivée": 1, "addup": 15}
{"départ": 2, "arrivée": 3, "addup": 6}

{"départ": 3, "arrivée": 1, "addup": 15}
{"départ": 3, "arrivée": 2, "addup": 22}



I'm going from 2 to 1.

I need to identify the possible paths.
if there is a bus line from 2 to 1,
    add the waiting time of the departure city and the travel time.
if there is a bus line from 2 to x to 1,
    add the waiting time of 2, x and the travel time.
if there is a bus line from 2 to a station connected to 1,
    add the waiting time of 2 and the travel time.

Problem : Can 2 access 1 from 3 ?
2 can access 1 from 3 if there is a path between 2 and 3 AND a path between 3 and 1
"""


"""
Calcul à faire dans l'ordre :
Ville 1 vers 2
5 + 2 = 7
Ville 1 vers 3
5 + 2 + 5 + 1 = 13
13 + 7 / 2 = 10
Moyenne = 10

Ville 2 vers 3
5 + 1 = 6
Ville 2 vers 1
5 + 5 + 10 + 5 = 25
Ville 2 vers 1 (par la gare)
5 + 5 + 5 = 15
15 + 6 / 2 = 10
Moyenne = 10

Ville 3 vers 1
10 + 5 = 15
Ville 3 vers 2
10 + 5 + 5 + 2 = 22
15 + 22 / 2 = 18
Moyenne = 18"""