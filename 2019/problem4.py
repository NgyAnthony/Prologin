"""
3 3 0 # n ; m ; g
n, le nombre de villes ;
m, le nombre de lignes de bus joignant les villes ;
g, le nombre de lignes de bus à directions de gares routières.

3 # Waiting time for the bus of the city n°1
10
5
1 2 4
2 3 5
1 3 2 # Shooter ; Target ; Travel time
identity :
    "ville" :
    "waiting_time":

trajet_ville :
    "depart" :
    "arrivée" :
    "tps_trajet" :

trajet_gare :

###########
list_id = [{"ville":"1","waiting_time":"5"}, {"ville":"2","waiting_time":"5"}, {"ville":"3","waiting_time":"10"}]
list_trajetv =[{"départ":"1", "arrivée":"2", "tps_trajet":"2"}, {"départ":"2", "arrivée":"1", "tps_trajet":"20"},
{"départ":"3", "arrivée":"1", "tps_trajet":"5"}, {"départ":"2", "arrivée":"3",) "tps_trajet":"1"}]
list_trajetg =[{"départ":"2", "arrivée":"3", "tps_trajet":5}]

id = {"ville":"1","waiting_time":"15"}
trajet_ville = {"départ":"1", "arrivée":"2", "tps_trajet":5}
trajet_gare = {"départ":"1", "arrivée":"2", "tps_trajet":0}


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
Moyenne = 18

###
Calcul à faire :

Ville 1 vers 2
3 + 4 = 7
Ville 1 vers 3
3 +2 = 5

Moyenne = 6
Ville 2 vers 3
10 + 5 = 15

Ville 3
-1

"""

(n, m, g) = list(map(int, "3 3 0".split()))
waiting_time = []
for i in range(n):
    waiting_time.insert(n, input("Temps d'attente de la ville n° %d" % (i + 1)))

for x in range(m):