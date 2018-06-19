ovaal = 0
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

    def __init__(self, aantal = 0, vorm = 0, kleur = 0, vulling = 0):
        self.aantal = aantal
        self.vorm = vorm
        self.kleur = kleur
        self.vulling = vulling

    def derde_kaart(self, other):

        kaart_3 == set_kaart()

        if if (self.aantal + other.aantal)%3 == 0:
            kaart_3.aantal == self.aantal + other.aantal
        if (self.aantal + other.aantal)%3 == 1:
            kaart_3.aantal == self.aantal + other.aantal + 2
        if (self.aantal + other.aantal)%3 == 2:
            kaart_3.aantal == self.aantal + other.aantal + 1

        return kaart_3


    #def __add__ (self, other):
        #for i in range(4):
            #self[i] += other[i]
        #return self

    #def derde_kaart(self, other):

        #kaart_3 = self + other

        #for i in range(4):
            #if kaart_3[i]%3 == 1:
                #kaart_3[i] += 2
            #if kaart_3[i]%3 == 2:
                #kaart_3[i] += 1
