def arnaque_aerienne0(prix_initial, billets, n):
    if prix_initial < 1 or prix_initial > 2000:
        print("Contrainte: valeur invalide.")
        quit()

    if n < 1 or n > 100:
        print("Contrainte: valeur invalide.")
        quit()

    scam = []
    legit = []

    for i in range(n):
        if int(billets[i]) < prix_initial:
            scam.insert(1, int(billets[i]))
        else:
            legit.insert(1, int(billets[i]))

    minimum_scam = min(scam)

    if len(scam) >= 3:
        print("ARNAQUE !")
    elif len(scam) < 3:
        print("Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos !")


prix_initial = int(input())
n = int(input())
billets = list(map(int, input().split()))


arnaque_aerienne0(prix_initial, billets, n)
