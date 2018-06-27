import Klassen_en_functies as set



def startspel():
    set_stapel = set.maakstapel()
    tafel = set.kaartenoptafel()
    a = [int(i)  for i in input().split()]
    tafel.pop(a[0])
    return tafel
