x = int(raw_input("Koliko stevilk zelis izzrebati? "))


import random

def izzrebana_stevila(y):
    cifre = []
    for random_stevilo in range(1, y):
        random_stevilo = random.randint(1, 200)
        cifre.append(random_stevilo)
    for a in cifre:
        print a


izzrebana_stevila(x)

