import random

ovaal= 0
rechthoek = 1
golf = 2

blauw = 0
groen = 1
roze = 2

leeg = 0
vol = 1
gespikkeld = 2

een = 0
twee = 1
drie = 2


class set_kaart:

    def __repr__(self):
        return (f'{self.__class__.__qualname__}'
                f'(aantal={self.aantal},vorm={self.vorm},'
                f'kleur={self.kleur},vulling={self.vulling})')

    def __init__(self, aantal = 0, vorm = 0, kleur = 0, vulling = 0):
        self.aantal = aantal
        self.vorm = vorm
        self.kleur = kleur
        self.vulling = vulling

    def derde_kaart(self, other):

        kaart_3 = set_kaart()

        def eigenschap_kaart(set_kaart, eigenschap, eigenschap_1, eigenschap_2):

            if (eigenschap_1 + eigenschap_2)%3 == 1:
                set_kaart.eigenschap = 2
            if (eigenschap_1 + eigenschap_2)%3 == 2:
                set_kaart.eigenschap = 1

            return set_kaart.eigenschap

        kaart_3.aantal = eigenschap_kaart(kaart_3, 'aantal', self.aantal, other.aantal)
        kaart_3.vorm = eigenschap_kaart(kaart_3, 'vorm', self.vorm, other.vorm)
        kaart_3.kleur = eigenschap_kaart(kaart_3, 'kleur', self.kleur, other.kleur)
        kaart_3.vulling = eigenschap_kaart(kaart_3, 'vulling', self.vulling, other.vulling)

        return kaart_3

def maakstapel():
    set_stapel = []
    for i in range (3):
        for j in range (3):
            for k in range (3):
                for l in range (3):
                    set_stapel.append(set_kaart(i,j,k,l))
    return(set_stapel)

def kaartenoptafel():
    kaarten_tafel: []
    
        set_stapel.pop(random.randrange(0,len(set_stapel)))
a = set_kaart(twee,golf,blauw,gespikkeld)
b = set_kaart(een,rechthoek,groen,leeg)
#:)
print(a.derde_kaart(b))
set_stapel = maakstapel()
print(set_stapel.pop(random.randrange(0,len(set_stapel)))) #haalt willekeurige kaart uit stapel
