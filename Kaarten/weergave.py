'''Uitleg van het document'''

import pygame as pg
import Klassen_en_functies as kf

def weergeef(kaarten_op_tafel):
    '''Uitleg van de functie'''
    pg.init()

    screen = pg.display.set_mode((450, 800))
    screen.fill((255, 255, 255))

    #Laad afbeelding en pas grootte aan
    #kaarten_op_tafel=kf.kaarten_op_tafel()

    b1 = pg.image.load(str(kaarten_op_tafel[0])+'.png')
    k1 = pg.transform.scale(b1, (150, 200))

    b2 = pg.image.load(str(kaarten_op_tafel[1])+'.png')
    k2 = pg.transform.scale(b2, (150, 200))

    b3 = pg.image.load(str(kaarten_op_tafel[2])+'.png')
    k3 = pg.transform.scale(b3, (150, 200))

    b4 = pg.image.load(str(kaarten_op_tafel[3])+'.png')
    k4 = pg.transform.scale(b4, (150, 200))

    b5 = pg.image.load(str(kaarten_op_tafel[4])+'.png')
    k5 = pg.transform.scale(b5, (150, 200))

    b6 = pg.image.load(str(kaarten_op_tafel[5])+'.png')
    k6 = pg.transform.scale(b6,(150,200))

    b7 = pg.image.load(str(kaarten_op_tafel[6])+'.png')
    k7 = pg.transform.scale(b7, (150, 200))

    b8= pg.image.load(str(kaarten_op_tafel[7])+'.png')
    k8 = pg.transform.scale(b8, (150, 200))

    b9 = pg.image.load(str(kaarten_op_tafel[8])+'.png')
    k9 = pg.transform.scale(b9, (150, 200))

    b10 = pg.image.load(str(kaarten_op_tafel[9])+'.png')
    k10 = pg.transform.scale(b10, (150, 200))

    b11 = pg.image.load(str(kaarten_op_tafel[10])+'.png')
    k11 = pg.transform.scale(b11, (150, 200))

    b12 = pg.image.load(str(kaarten_op_tafel[11])+'.png')
    k12 = pg.transform.scale(b12, (150, 200))

    #Plaats de kaarten
    screen.blit(k1, (0, 0))
    screen.blit(k2, (150, 0))
    screen.blit(k3, (300, 0))
    screen.blit(k4, (0, 200))
    screen.blit(k5, (150, 200))
    screen.blit(k6, (300, 200))
    screen.blit(k7, (0, 400))
    screen.blit(k8, (150, 400))
    screen.blit(k9, (300, 400))
    screen.blit(k10, (0, 600))
    screen.blit(k11, (150, 600))
    screen.blit(k12, (300, 600))

    #Laat de kaarten zien
    pg.display.update()
def ververs_weergave(kaarten_op_tafel):
    '''Uitleg van de functie'''
    #Laad afbeelding en pas grootte aan
    #kaarten_op_tafel=kf.kaarten_op_tafel()

    b1 = pg.image.load(str(kaarten_op_tafel[0])+'.png')
    k1 = pg.transform.scale(b1, (150, 200))

    b2 = pg.image.load(str(kaarten_op_tafel[1])+'.png')
    k2 = pg.transform.scale(b2, (150, 200))

    b3 = pg.image.load(str(kaarten_op_tafel[2])+'.png')
    k3 = pg.transform.scale(b3, (150, 200))

    b4 = pg.image.load(str(kaarten_op_tafel[3])+'.png')
    k4 = pg.transform.scale(b4, (150, 200))

    b5 = pg.image.load(str(kaarten_op_tafel[4])+'.png')
    k5 = pg.transform.scale(b5, (150, 200))

    b6 = pg.image.load(str(kaarten_op_tafel[5])+'.png')
    k6 = pg.transform.scale(b6, (150, 200))

    b7 = pg.image.load(str(kaarten_op_tafel[6])+'.png')
    k7 = pg.transform.scale(b7, (150, 200))

    b8= pg.image.load(str(kaarten_op_tafel[7])+'.png')
    k8 = pg.transform.scale(b8, (150, 200))

    b9 = pg.image.load(str(kaarten_op_tafel[8])+'.png')
    k9 = pg.transform.scale(b9, (150, 200))

    b10 = pg.image.load(str(kaarten_op_tafel[9])+'.png')
    k10 = pg.transform.scale(b10, (150, 200))

    b11 = pg.image.load(str(kaarten_op_tafel[10])+'.png')
    k11 = pg.transform.scale(b11, (150, 200))

    b12 = pg.image.load(str(kaarten_op_tafel[11])+'.png')
    k12 = pg.transform.scale(b12, (150, 200))

    #Plaats de kaarten
    screen.blit(k1, (0, 0))
    screen.blit(k2, (150, 0))
    screen.blit(k3, (300, 0))
    screen.blit(k4, (0, 200))
    screen.blit(k5, (150, 200))
    screen.blit(k6, (300, 200))
    screen.blit(k7, (0, 400))
    screen.blit(k8, (150, 400))
    screen.blit(k9, (300, 400))
    screen.blit(k10, (0, 600))
    screen.blit(k11, (150, 600))
    screen.blit(k12, (300, 600))

    #Laat de kaarten zien
    pg.display.update()
