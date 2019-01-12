list_trajetv =[{"départ": 1, "arrivée": 2, "tps_trajet": 2}, {"départ": 2, "arrivée": 1, "tps_trajet": 20},
{"départ": 3, "arrivée": 1, "tps_trajet": 5}, {"départ": 2, "arrivée": 3, "tps_trajet": 1}]
list_trajetg =[{"départ": 2, "arrivée": 3, "tps_trajet": 5}]

#print(len(list_trajetv))
#print(list_trajetv[1].get('arrivée'))
arrival_list = []
for x in range(len(list_trajetv)):
    ar_v = list_trajetv[x].get('arrivée')
    arrival_list.append(ar_v)
for a in range(len(list_trajetg)):
    ar_g = list_trajetg[a].get('arrivée')
    arrival_list.append(ar_g)
arrival_list = list(set(arrival_list))

print(arrival_list)