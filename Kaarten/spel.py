'''Uitleg van dit document'''

import random
import time
import pygame
import Klassen_en_functies as klasse
import gui

def start_spel():
    '''Uitleg van de functie'''
    print("Leuk dat je Set! gaat spelen. Wat is je naam?") #intro van het spel
    naam = input()

    print ("Hallo", naam, ". Welke moeilijkheidsgraad wil je: makkelijk, normaal, moeilijk, extreem?")
    invoer_moeilijkheidsgraad = input()
    #bepaalt de tijd
    if invoer_moeilijkheidsgraad == "makkelijk":
        tijd = 60
    if invoer_moeilijkheidsgraad == "normaal":
        tijd = 30
    if invoer_moeilijkheidsgraad == "moeilijk":
        tijd = 20
    if invoer_moeilijkheidsgraad == "extreem":
        tijd = 12

    print("Heel veel succes", naam, "! De kaarten komen er aan!")

    time.sleep(3)               #wacht drie seconden tot het spel begint
    punten_speler = 0            #zet punten van beide spelers op 0
    punten_computer = 0
    set_stapel = klasse.maak_stapel()  #stapel met kaarten
    tafel = klasse.kaarten_op_tafel(set_stapel) #kaarten die op de tafel liggen
    #Laat de kaarten op tafel zien
    gui.weergave(tafel)
    #while len(set_stapel) >= 0 and len(tafel)==12: #
        #gui.weergave(tafel)
    #    start = time.perf_counter() #begin van je denktijd
    #    speler_invoer = [int(i)-1  for i in input().split()]

    #    geldigheid_invoer = (len(speler_invoer) == 3 and 0<=speler_invoer[0]<=11
    #        and 0<=speler_invoer[1]<=11 and 0<=speler_invoer[2]<=11)
        #kijkt of het een geldige invoer is

    #    if geldigheid_invoer == True:
    #        set_klopt =  (klasse.set_kaart.derde_kaart(tafel[speler_invoer[0]],
    #        tafel[speler_invoer[1]]) == tafel[speler_invoer[2]])
           #kijkt of de set geldig is
    #   else:
    #       set_klopt = False

    #   if time.perf_counter() - start < tijd and geldigheid_invoer == True:
            #alleen als de set binnen de tijd is en geldig is
    #        set_klopt == True
    '''Deze functie is het hele spel'''
    #punten_speler = 0
    #punten_computer = 0
    #set_stapel = klasse.maak_stapel()
    #tafel = klasse.kaarten_op_tafel()
    while len(set_stapel) > 2:
        gui.weergave(tafel)
        #print(tafel)
        start = time.perf_counter()
        if time.perf_counter() - start < 5:
            speler_invoer = [int(i)  for i in input().split()]
            if (klasse.set_kaart.derde_kaart(tafel[speler_invoer[0]],
            tafel[speler_invoer[1]]) == tafel[speler_invoer[2]]):
                indices = speler_invoer[0], speler_invoer[1], speler_invoer[2]
                tafel = [i for j, i in enumerate(tafel) if j not in indices]
                #haalt de set weg
                punten_speler += 1
                print("Goed zo!")
                if len(set_stapel) >=3:
                    for i in range(3):
                        nieuwe_kaart = set_stapel.pop(random.randrange(0,len(set_stapel)))
                        tafel.append(nieuwe_kaart) # vult tafel weer aan
            else:
                print("Dit is een helaas geen set.")

        if klasse.vind_alle_sets(tafel) == []: #er zijn geen sets op tafel
            print("Er ligt geen set, we vervangen drie kaarten.")
            indices = 0, 1, 2
            tafel = [i for j, i in enumerate(tafel) if j not in indices]
            #verwijdert eerste 3 kaarten
            if len(set_stapel) >=3:
                for i in range(3):
                    nieuwe_kaart = set_stapel.pop(random.randrange(0,len(set_stapel)))
                    tafel.append(nieuwe_kaart)
                    gui.ververs_weergave()
        if klasse.vind_alle_sets(tafel) == []:
                indices = 0, 1, 2
                tafel = [i for j, i in enumerate(tafel) if j not in indices]
                for i in range(3):
                    nieuwe_kaart = set_stapel.pop(random.randrange(0,len(set_stapel)))
                    tafel.append(nieuwe_kaart) #voegt weer 3 kaarten toe
                    gui.ververs_weergave(tafel)
        elif (time.perf_counter() - start >= tijd or
              set_klopt == False or geldigheid_invoer == False):
            #situaties waarbij de computer een set pakt
            if time.perf_counter() - start >= tijd: #je bent te langzaam
                print("Helaas je bent te laat,",naam, ". De computer heeft al een set gevonden.")
            if geldigheid_invoer == False: #de invoer was ongeldig
                print( "Deze invoer is niet mogelijk.")

            sets = klasse.vind_alle_sets(tafel) #computer pakt een set
        elif (time.perf_counter() - start >= 5 or
              klasse.set_kaart.derde_kaart(tafel[speler_invoer[0]], tafel[a[1]]) != tafel[a[2]]):
            sets = klasse.vind_alle_sets(tafel)
            drie_kaarten = random.choice(sets)
            tafel.remove(drie_kaarten[2]) #set wordt verwijderd van de tafel
            tafel.remove(drie_kaarten[1])
            tafel.remove(drie_kaarten[0])
            punten_computer += 1
            if len(set_stapel) >=3: # de tafel wordt weer aangevuld
                for i in range(3):
                        a = set_stapel.pop(random.randrange(0,len(set_stapel)))
                        tafel.append(a)
                        gui.ververs_weergave()
    if punten_speler < punten_computer: #boodschap voor het einde
        boodschap = "Je hebt dus helaas verloren. Volgende keer beter."
    if punten_speler > punten_computer:
        boodschap = "Je hebt dus gewonnen. Gefeliciteerd!"
    if punten_speler == punten_computer:
        boodschap = "Het is gelijkspel geworden."
    pygame.quit()
    return print(naam, ",je hebt", punten_speler , "punten en de computer heeft"
                 , punten_computer , "punten.", boodschap) #einde spel


start_spel()
