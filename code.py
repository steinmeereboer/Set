class set_kaart:

    def __init__(self, aantal = 0, vorm = 0, kleur = 0, vulling = 0):
        self.aantal = aantal
        self.vorm = vorm
        self.kleur = kleur
        self.vulling = vulling


    def __add__ (self, other):
        for i in range(4):
            self[i] += other[i]
        return self

    def derde_kaart(self, other):

        kaart_3 = self + other

        for i in range(4):
            if kaart_3[i]%3 == 1:
                kaart_3[i] += 2
            if kaart_3[i]%3 == 2:
                kaart_3[i] += 1
