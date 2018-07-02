'''Dit is de opdracht Set! van Fien, Stein en Olaf.'''

import random
import time
import pygame
import Klassen_en_functies as klasse
import gui

def kaarten_toevoegen(set_stapel, tafel):
    '''Functie die kaarten aan de tafel toevoegt'''
    if len(set_stapel) >= 3:
        #Er worden drie willekeurige kaarten van set_stapel aan tafel toegevoegd
        for i in range(3):
            nieuwe_kaart = set_stapel.pop(random.randrange(0, len(set_stapel)))
            tafel.append(nieuwe_kaart)

def intro_naam():
    '''Functie die vraagt om de naam van de speler'''
    #De introductie van het spel
    print("Leuk dat je Set! gaat spelen. Wat is je naam?")
    naam = input()
    return naam

def tijd_keuze(naam):
    '''Functie die de moeilijkheidsgraad bepaalt, en daarmee de tijd'''
    print("Hallo", naam,
          ".Welke moeilijkheidsgraad wil je: makkelijk, normaal, moeilijk, extreem?")
    invoer_moeilijkheidsgraad = input()
    while invoer_moeilijkheidsgraad not in  ["makkelijk", "normaal", "moeilijk", "extreem"]:
        print("Dit is helaas niet mogelijk,"
              "probeer het opnieuw: makkelijk, normaal, moeilijk, extreem.")
        invoer_moeilijkheidsgraad = input()

    #Hier wordt de tijd bepaald
    if invoer_moeilijkheidsgraad == "makkelijk":
        tijd = 40
    if invoer_moeilijkheidsgraad == "normaal":
        tijd = 25
    if invoer_moeilijkheidsgraad == "moeilijk":
        tijd = 15
    if invoer_moeilijkheidsgraad == "extreem":
        tijd = 10

    print("Heel veel succes", naam, "! De kaarten komen er aan!")

    return tijd

def start_spel():
    '''Functie die het spel is'''
    naam = intro_naam()
    tijd = tijd_keuze(naam)

    #Er wordt drie seconden gewacht tot het spel begint
    time.sleep(3)
    #De punten van beide spelers worden op 0 gezet
    punten_speler = 0
    punten_computer = 0
    #De stapel met kaarten wordt gemaakt
    set_stapel = klasse.maak_stapel()
    #Er worden twaalf kaarten op tafel gelegd
    tafel = klasse.kaarten_op_tafel(set_stapel)

    #De kaarten op tafel worden afgebeeld op het beeldscherm
    #Het spel gaat door totdat er geen twaalf kaarten meer op tafel liggen
    while len(tafel) >= 12:
        gui.weergave(tafel)
        start = time.perf_counter()

        #Controleren of er wel sets op tafel liggen
        while klasse.vind_alle_sets(tafel) == [] and len(tafel) >= 12:
            print("Er ligt geen set, we hebben drie kaarten vervangen.")
            #De eerste drie kaarten worden verwijderd
            indices = 0, 1, 2
            tafel = [i for j, i in enumerate(tafel) if j not in indices]
            kaarten_toevoegen(set_stapel, tafel)

        speler_invoer = [int(i)-1  for i in input().split()] #invoer van de speler

        #Controleren of de invoer van de speler geldig is
        geldigheid_invoer = (len(speler_invoer) == 3 and 0 <= speler_invoer[0] <= 11
                             and 0 <= speler_invoer[1] <= 11 and 0 <= speler_invoer[2] <= 11)

        #Controleren of de invoer een set is
        if geldigheid_invoer is True:
            set_klopt = (klasse.set_kaart.derde_kaart(tafel[speler_invoer[0]],
                         tafel[speler_invoer[1]]) == tafel[speler_invoer[2]])
        else:
            set_klopt = False

        #Dit is als de invoer geldig is, de invoer een set is en de speler op tijd is
        if time.perf_counter() - start < tijd and set_klopt is True:
            indices = speler_invoer[0], speler_invoer[1], speler_invoer[2]
            #De set wordt uit de kaarten op tafel gehaald
            tafel = [i for j, i in enumerate(tafel) if j not in indices]
            #De speler krijgt een punt
            punten_speler += 1
            print("Goed zo!")
            #Er worden drie kaarten toegevoegd aan de tafel
            kaarten_toevoegen(set_stapel, tafel)

        #Dit is als de speler te langzaam is, de invoer niet geldig of de invoer geen set is
        elif ((time.perf_counter() - start >= tijd or
               set_klopt is False or geldigheid_invoer is False)
              and klasse.vind_alle_sets(tafel) != []):
            #Wanneer de speler te langzaam is
            if time.perf_counter() - start >= tijd:
                print("Helaas je bent te laat,", naam)
            #Wanneer de invoer ongeldig is
            elif geldigheid_invoer is False:
                print("Deze invoer is niet mogelijk.")
            #Wanneer de invoer geen set is
            elif set_klopt is False:
                print("Dit was helaas geen set.")

            #De computer kiest willekeurig een set van de sets op tafel
            sets = klasse.vind_alle_sets(tafel)
            drie_kaarten = random.choice(sets)

            #De set van de computer wordt getoond en de speler kan hier vijf seconden naar kijken
            print("De computer heeft wel een set gevonden:", tafel.index(drie_kaarten[0])+1,
                  tafel.index(drie_kaarten[1])+1, tafel.index(drie_kaarten[2])+1)
            time.sleep(5)

            #De set wordt verwijderd van de tafel
            for i in range(3):
                tafel.remove(drie_kaarten[i])

            #De computer krijgt een punt
            punten_computer += 1
            kaarten_toevoegen(set_stapel, tafel)

    #De laatste boodschap voor de speler
    if punten_speler < punten_computer:
        boodschap = "Je hebt dus helaas verloren. Volgende keer beter."
    if punten_speler > punten_computer:
        boodschap = "Je hebt dus gewonnen. Gefeliciteerd!"
    if punten_speler == punten_computer:
        boodschap = "Het is gelijkspel geworden."
    pygame.quit()

    return print(naam, ",je hebt", punten_speler, "punten en de computer heeft"
                 , punten_computer, "punten.", boodschap) #einde spel


start_spel()
