'''In dit document staat de klasse van setkaarten en de bijbehorende functies'''

# pylint: disable = C0103

import random
from itertools import combinations, product

OVAAL, RECHTHOEK, GOLF = range(3)
BLAUW, GROEN, ROZE = range(3)
LEEG, VOL, GESTREEPT = range(3)
EEN, TWEE, DRIE = range(3)

class set_kaart:
    '''Deze klasse definieert de eigenschappen van een setkaart'''


    def __eq__(self, other):
        ''''Functie die bepaalt wanneer twee setkaarten gelijk zijn aan elkaar'''
        return (self.aantal == other.aantal and self.vorm == other.vorm
                and self.kleur == other.kleur and self.vulling == other.vulling)

    def __repr__(self):
        return (f'{self.__class__.__qualname__}'
                f'(aantal={self.aantal},vorm={self.vorm},'
                f'kleur={self.kleur},vulling={self.vulling})')

    def __init__(self, aantal=0, vorm=0, kleur=0, vulling=0):
        '''Functie die de eigenschappen van een setkaart bepaalt'''
        self.aantal = aantal
        self.vorm = vorm
        self.kleur = kleur
        self.vulling = vulling

    def derde_kaart(self, other):
        '''Functie die bij twee setkaarten een derde kaart vindt zodat ze samen een set vormen'''

        kaart_3 = set_kaart()

        def eigenschap_kaart(eigenschap_1, eigenschap_2):
            '''Functie die de eigenschappen van de derde kaart bepaalt'''
            lijst = [0, 2, 1]
            return lijst[(eigenschap_1 + eigenschap_2)%3]

        kaart_3.aantal = eigenschap_kaart(self.aantal, other.aantal)
        kaart_3.vorm = eigenschap_kaart(self.vorm, other.vorm)
        kaart_3.kleur = eigenschap_kaart(self.kleur, other.kleur)
        kaart_3.vulling = eigenschap_kaart(self.vulling, other.vulling)

        return kaart_3

def vind_set(lijst):
    '''Functie die een set vindt in een lijst van setkaarten'''
    for kaart_1, kaart_2 in combinations(lijst, 2):
        kaart_3 = set_kaart.derde_kaart(kaart_1, kaart_2)
        if kaart_3 in lijst:
            return [kaart_1, kaart_2, kaart_3]
    return None

def vind_alle_sets(lijst):
    '''Functie die alle sets vindt in een lijst van setkaarten'''
    alle_sets = []
    for kaart_1, kaart_2 in combinations(lijst, 2):
        kaart_3 = set_kaart.derde_kaart(kaart_1, kaart_2)
        if kaart_3 in lijst:
            alle_sets.append((kaart_1, kaart_2, kaart_3))
    return alle_sets

def maak_stapel():
    '''Functie die de 81 unieke setkaarten maakt en hier een stapel van maakt'''
    set_stapel = []
    for i, j, k, l in product(range(3), range(3), range(3), range(3)):
        set_stapel.append(set_kaart(i, j, k, l))
    return set_stapel

def kaarten_op_tafel(lijst):
    '''Functie die 12 willekeurige kaarten uit de stapel kiest en
       toevoegt aan de kaarten op tafel'''
    tafelkaarten = [set_kaart()]*12
    for i in range(12):
        setkaart = lijst.pop(random.randrange(0, len(lijst)))
        tafelkaarten[i] = setkaart
    return tafelkaarten
