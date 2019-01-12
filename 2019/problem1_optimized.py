prix_initial = int(input())
n = int(input())
billets = list(map(int, input().split()))


def find_errors():
    if n < 1 or n > 100:
        print("Contrainte: valeur invalide.")
        quit()
    if prix_initial < 1 or prix_initial > 2000:
        print("Contrainte: valeur invalide.")
        quit()


def find_scam():
    scam = []
    for i in range(n):
        if int(billets[i]) < prix_initial:
            scam.insert(1, int(billets[i]))

    if len(scam) >= 3:
        print("ARNAQUE !")
    elif len(scam) < 3:
        print("Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos !")


def start():
    find_errors()
    find_scam()

start()


def arnaque_aerienne0(prix_initial, billets, n):
    pass
prix_initial = int(input())
n = int(input())
billets = list(map(int, input().split()))
arnaque_aerienne0(prix_initial, billets, n)