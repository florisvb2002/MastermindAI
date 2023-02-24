# Importeer Nodige functies

from Feedback import *


def keuze_menu():

    '''
    Functie voor het keuze menu
    Laat alle opties zien en de gebruiker kan daaruit kiezen
    :return: optie
    '''

    # Print alle opties
    print('Optie 1: Probeer het zelf')
    print('Optie 2: Laat AI het werk doen door middel van worst case scenerio')
    print('Optie 3: Laat AI het werk doen door middel van expected case scenerio')
    print('Optie 4: Laat AI het werk doen door middel van dumb case scenerio')

    # De gebruiker vult een optie in
    optie = input('Kies 1 van de opties hierboven: ')

    # Return optie
    return optie


def keuze(optie, mogelijkheden):
    '''
    Kijkt welke optie de gebruiker heeft gekozen
    :return: Het Algoritme of Zelf raden
    '''

    # Kijkt of het optie 1 is
    if optie == '1':
        # Return gebruiker zelf laten kiezen
        return vraag_input()

    # Kijkt of het optie 2 is
    elif optie == '2':
        # Return worst case scenario
        return worst_case(mogelijkheden)

    # Kijkt of het optie 3 is
    elif optie == '3':
        # Return expected case scenario
        return expected_case(mogelijkheden)

    # Kijkt of het optie 4 is
    elif optie == '4':
        # Return dumb case scenario
        return dumb_case(mogelijkheden)

    # Wat anders dan de opties is gebruiker zelf laten kiezen
    else:
        return vraag_input()