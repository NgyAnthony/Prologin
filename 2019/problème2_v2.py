n = int(input())

liste_p = [None] * n
if n < 1 or n > 1000:
    print('Contrainte: valeur invalide.')
    quit()

for i in range(0, n):
    try: (id, decalage) = list(map(int, input().split()))
    except ValueError:
        print("Contrainte: Le format n'est pas respecté")
    lieux_i = {"id": id, "decalage": decalage}
    liste_p[i] = lieux_i

    for l in range(0, i):
        if int(liste_p[i].get('id') == liste_p[l].get('id')):
            print("Contrainte: l'ID du pays est déjà utilisé.")
            quit()

    if liste_p[i].get('decalage') < -12 or liste_p[i].get('decalage') > 12:
        print('Contrainte: le décalage est invalide.')
        quit()

v = int(input())
if v < 1 or v > 1000:
    print("Contrainte: la valeur 'nombre de voyages' n'est pas respectée.")
    quit()

liste_e = [None] * v
for j in range(0, v):
    try: (voyageur, destination) = list(map(int, input().split()))
    except ValueError:
        print("Contrainte: Le format n'est pas respecté")
    etape_i = {"voyageur": voyageur, "destination": destination}
    liste_e[j] = etape_i
    if liste_e[j].get('voyageur') < 1 or liste_e[j].get('voyageur') > 1000:
        print('Contrainte: la valeur "voyageur" est invalide.')
        quit()

    id_values = []
    for r in range(0, v):
        id_values.insert(0, liste_p[r].get('id'))

    if liste_e[j].get('destination') not in id_values:
        print("Contrainte: il n'y a pas de destination correspondant à cet ID.")
        quit()

    if liste_e[j].get("destination") > 12 or liste_e[j].get("destination") < -12:
        print('Contrainte: la valeur "destination" est invalide.')
        quit()


def meli_melo_temporel0(lieux, etapes, v):
    gmt_v1 = 0
    gmt_v2 = 0
    for p in range(0, v):
        if etapes[p].get('voyageur') == 1:
            destination = int(etapes[p].get('destination'))
            decalage = lieux[destination - 1].get('decalage')
            gmt_v1 = decalage
        elif etapes[p].get('voyageur') == 2:
            destination = int(etapes[p].get('destination'))
            decalage = lieux[destination - 1].get('decalage')
            gmt_v2 = decalage
        distance = abs(gmt_v1 - gmt_v2)
        print(distance)


meli_melo_temporel0(liste_p, liste_e, v)