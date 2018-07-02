'''Deze code zorgt voor een visualisatie van de kaarten'''

import pygame as pg
import Klassen_en_functies

#Klassen en functies hebben wij nodig voor de string functie van een kaart

#Initialiseer pygame
pg.init()
#Het lettertype Arial wordt geladen met grootte 15
font = pg.font.SysFont('Arial', 15)

def weergave(kaarten_op_tafel):
    '''Functie die een lijst kaarten_op_tafel inleest en deze afbeeldt op het beeldscherm'''

    #Initialiseer een scherm met afmeting 450x800
    screen = pg.display.set_mode((450, 800))
    #Vul het scherm wit
    screen.fill((255, 255, 255))                            

    #Laad afbeelding en pas grootte aan

    b1 = pg.image.load(str(kaarten_op_tafel[0])+'.png')     #Laad kaart 1
    k1 = pg.transform.scale(b1, (150, 200))                 #Schaal de kaart naar 150x200 zodat er 3x4 kaarten
                                                            #Op 450x800 kan afgebeeld worden
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

    #Laad de labels
    lab1 = font.render("1", 1, (0, 0, 0))
    lab2 = font.render("2", 1, (0, 0, 0))
    lab3 = font.render("3", 1, (0, 0, 0))
    lab4 = font.render("4", 1, (0, 0, 0))
    lab5 = font.render("5", 1, (0, 0, 0))
    lab6 = font.render("6", 1, (0, 0, 0))
    lab7 = font.render("7", 1, (0, 0, 0))
    lab8 = font.render("8", 1, (0, 0, 0))
    lab9 = font.render("9", 1, (0, 0, 0))
    lab10 = font.render("10", 1, (0, 0, 0))
    lab11 = font.render("11", 1, (0, 0, 0))
    lab12 = font.render("12", 1, (0, 0, 0))

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

    #Plaats de labels
    screen.blit(lab1, (75, 183))
    screen.blit(lab2, (225, 183))
    screen.blit(lab3, (375, 183))
    screen.blit(lab4, (75, 383))
    screen.blit(lab5, (225, 383))
    screen.blit(lab6, (375, 383))
    screen.blit(lab7, (75, 583))
    screen.blit(lab8, (225, 583))
    screen.blit(lab9, (375, 583))
    screen.blit(lab10, (75, 783))
    screen.blit(lab11, (225, 783))
    screen.blit(lab12, (375, 783))



    #Laat de kaarten zien
    pg.display.update()
