import Klassen_en_functies as set
import random


def startspel():
    set_stapel = set.maakstapel()
    tafel = set.kaartenoptafel()
    while len(set_stapel) != 0:
        speler_invoer = [int(i) for i in input().split()]
        if (set.set_kaart.derde_kaart(tafel[speler_invoer[0]],
            tafel[speler_invoer[1]]) == tafel[speler_invoer[2]]):
            indices = speler_invoer[0], speler_invoer[1], speler_invoer[2]
            tafel = [i for j, i in enumerate(tafel) if j not in indices]

            for i in range(3):
                nieuwe_kaart = set_stapel.pop(random.randrange(0,len(set_stapel)))
                tafel.append(nieuwe_kaart)

        print(tafel)
    return tafel

set_stapel = set.maakstapel()
