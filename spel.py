import Klassen_en_functies as set
import random


def startspel():
    set_stapel = set.maakstapel()
    tafel = set.kaartenoptafel()
    while len(set_stapel) > 2:
        print(set.set_kaart.vind_alle_set(tafel))
        print(tafel)
        a = [int(i)  for i in input().split()]
        if set.set_kaart.derde_kaart(tafel[a[0]], tafel[a[1]]) == tafel[a[2]]:
            indices = a[0], a[1], a[2]
            tafel = [i for j, i in enumerate(tafel) if j not in indices]
            for i in range(3):
                a = set_stapel.pop(random.randrange(0,len(set_stapel)))
                tafel.append(a)
        print(tafel)
    return tafel

set_stapel = set.maakstapel()
