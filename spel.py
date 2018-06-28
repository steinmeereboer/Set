import Klassen_en_functies as set
import random
import time


def startspel():
    set_stapel = set.maakstapel()
    tafel = set.kaartenoptafel()
    while len(set_stapel) > 2:
        print(tafel)
        start = time.perf_counter()
        if time.perf_counter()-start<5:
            a = [int(i)  for i in input().split()]
            if set.set_kaart.derde_kaart(tafel[a[0]], tafel[a[1]]) == tafel[a[2]]:
                indices = a[0], a[1], a[2]
                tafel = [i for j, i in enumerate(tafel) if j not in indices]
    
                for i in range(3):
                    a = set_stapel.pop(random.randrange(0,len(set_stapel)))
                    tafel.append(a)
                    
        if set.set_kaart.vind_alle_set(tafel) == []:
                indices = 0, 1, 2
                tafel = [i for j, i in enumerate(tafel) if j not in indices]
                for i in range(3):
                    nieuwe_kaart = set_stapel.pop(random.randrange(0,len(set_stapel)))
                    tafel.append(nieuwe_kaart)           
                    
        elif (time.perf_counter()-start>= 5 or 
            set.set_kaart.derde_kaart(tafel[a[0]], tafel[a[1]]) != tafel[a[2]]):
            sets = set.set_kaart.vind_alle_set(tafel)
            driekaarten = random.choice(sets)
            tafel.remove(driekaarten[2])
            tafel.remove(driekaarten[1])
            tafel.remove(driekaarten[0])
            for i in range(3):
                    a = set_stapel.pop(random.randrange(0,len(set_stapel)))
                    tafel.append(a)   
            
            
        
    return 128


startspel()
