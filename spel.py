import Klassen_en_functies as set
import random
import time

def start_spel():
    punten_speler = 0
    punten_computer = 0
    set_stapel = set.maak_stapel()
    tafel = set.kaarten_op_tafel()
    while len(set_stapel) > 2:
        print(tafel)
        start = time.perf_counter()
        if time.perf_counter() - start < 5:
            speler_invoer = [int(i)  for i in input().split()]
            if (set.set_kaart.derde_kaart(tafel[speler_invoer[0]],
            tafel[speler_invoer[1]]) == tafel[speler_invoer[2]]):
                indices = speler_invoer[0], speler_invoer[1], speler_invoer[2]
                tafel = [i for j, i in enumerate(tafel) if j not in indices]
                punten_speler += 1

                for i in range(3):
                    nieuwe_kaart = set_stapel.pop(random.randrange(0,len(set_stapel)))
                    tafel.append(nieuwe_kaart)

        if set.set_kaart.vind_alle_sets(tafel) == []:
                indices = 0, 1, 2
                tafel = [i for j, i in enumerate(tafel) if j not in indices]
                for i in range(3):
                    nieuwe_kaart = set_stapel.pop(random.randrange(0,len(set_stapel)))
                    tafel.append(nieuwe_kaart)

        elif (time.perf_counter() - start >= 5 or
        set.set_kaart.derde_kaart(tafel[speler_invoer[0]], tafel[a[1]]) != tafel[a[2]]):
            sets = set.set_kaart.vind_alle_sets(tafel)
            drie_kaarten = random.choice(sets)
            tafel.remove(drie_kaarten[2])
            tafel.remove(drie_kaarten[1])
            tafel.remove(drie_kaarten[0])
            punten_computer += 1
            for i in range(3):
                    a = set_stapel.pop(random.randrange(0,len(set_stapel)))
                    tafel.append(a)

        return print("Jij hebt", punten_speler , "punten en de computer heeft"
                 , punten_computer , "punten. ")

start_spel()
