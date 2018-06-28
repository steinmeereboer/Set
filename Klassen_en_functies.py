import random

ovaal, rechthoek, golf = range(3)
blauw, groen, roze = range(3)
leeg, vol, gestreept = range(3)
een, twee, drie = range(3)

class set_kaart:

    def __eq__(self, other):
        return (self.aantal == other.aantal and self.vorm == other.vorm
                and self.kleur == other.kleur and self.vulling == other.vulling)

    def __repr__(self):
        return (f'{self.__class__.__qualname__}'
                f'(aantal={self.aantal},vorm={self.vorm},'
                f'kleur={self.kleur},vulling={self.vulling})')

    def __init__(self, aantal = 0, vorm = 0, kleur = 0, vulling = 0):
        self.aantal = aantal
        self.vorm = vorm
        self.kleur = kleur
        self.vulling = vulling

    #Functie die bij twee setkaarten een derde kaart vindt zodat ze samen een set vormen
    def derde_kaart(self, other):

        kaart_3 = set_kaart()

        #Functie die de eigenschappen van de derde kaart bepaalt
        def eigenschap_kaart(set_kaart, eigenschap, eigenschap_1, eigenschap_2):
            if (eigenschap_1 + eigenschap_2)%3 == 0:
                setkaart.eigenschap = 0
            if (eigenschap_1 + eigenschap_2)%3 == 1:
                setkaart.eigenschap = 2
            if (eigenschap_1 + eigenschap_2)%3 == 2:
                setkaart.eigenschap = 1
            return set_kaart.eigenschap

        kaart_3.aantal = eigenschap_kaart(kaart_3, 'aantal', self.aantal, other.aantal)
        kaart_3.vorm = eigenschap_kaart(kaart_3, 'vorm', self.vorm, other.vorm)
        kaart_3.kleur = eigenschap_kaart(kaart_3, 'kleur', self.kleur, other.kleur)
        kaart_3.vulling = eigenschap_kaart(kaart_3, 'vulling', self.vulling, other.vulling)

        return kaart_3

    #Functie die een set vindt in een lijst van setkaarten
    def vind_set(lijst):
        for kaart_1 in lijst:
            for kaart_2 in lijst:
                if kaart_2 != kaart_1:
                    for kaart_3 in lijst:
                        if  kaart_3 == set_kaart.derde_kaart(kaart_1, kaart_2):
                            return([kaart_1, kaart_2, kaart_3])
                            break

    #Functie die alle sets vindt in een lijst van setkaarten
    def vind_alle_sets(lijst):
        alle_sets = []
        for kaart_1 in lijst:
            for kaart_2 in lijst:
                if kaart_2 != kaart_1:
                    for kaart_3 in lijst:
                        if  kaart_3 == set_kaart.derde_kaart(kaart_1, kaart_2):
                            alle_sets.append([kaart_1, kaart_2, kaart_3])
        return(alle_sets)

#Functie die de 81 unieke setkaarten maakt en hier een stapel van maakt
def maak_stapel():
    set_stapel = []
    for i in range (3):
        for j in range (3):
            for k in range (3):
                for l in range (3):
                    set_stapel.append(set_kaart(i,j,k,l))
    return(set_stapel)

set_stapel = maak_stapel()

#Functie die 12 willekeurige kaarten uit de stapel kiest en toevoegt aan de kaarten op tafel
def kaarten_op_tafel():
    kaarten_op_tafel = []
    for i in range(12):
        setkaart = set_stapel.pop(random.randrange(0,len(set_stapel)))
        kaarten_tafel.append(setkaart)
    return kaarten_op_tafel

def zie_tafel():
    b = kaarten_op_tafel()
    print(b[0:3])
    print(b[3:6])
    print(b[6:9])
    print(b[9:12])
