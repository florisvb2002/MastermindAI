# Importeren van libraries (standaard geinstalleerd)
import random
import itertools


# Importeren van alle functies
from Feedback import *
from Menu import *
from Tools import *



# Globale variabelen voor de spelinstellingen kunnen makkelijk aangepast worden
# Lengte van de code
LENGTE = 4
# Lijst van de kleuren
KLEUREN = ['A', 'B', 'C', 'D', 'E', 'F']
# Bepaal het aantal gokken dat de gebruiker krijgt met de RickRegel
MAX_GUESSES = LENGTE + len(KLEUREN)
# Genereer alle combinaties (zodat we dit niet elke keer spelen opnieuw hoeven te doen)
PERMUTATIES = [code for code in itertools.product(KLEUREN, repeat=LENGTE)]
# Bepaal de voorbeelcode door middel van de lengte van de code en de kleuren
VOORBEELDCODE = ''.join(KLEUREN[:LENGTE])


# Importeer de opnieuw functie van de les
# Source: https://github.com/LinaBlijlevenHU/StructuredProgramming2023
def opnieuw():
    # Geef de gebruiker de mogelijkheid om opnieuw te spelen
    opnieuw = input("Wil je opnieuw spelen? Typ ja of nee: ")

    # Start het spel opnieuw indien nodig
    if (opnieuw == "ja"):
        main()



# Importeer de mastermind functie van de les
# Source: https://github.com/LinaBlijlevenHU/StructuredProgramming2023
def main():
    '''
    De main game functie (speelt één spel)
    '''
    print(f"Welkom bij Mastermind! Je kan kiezen uit de kleuren {KLEUREN}")

    # Laar de gebruiker de optie kiezen
    optie = keuze_menu()

    # Kies een geheime combinatie
    secret = random.choice(PERMUTATIES)
    print(secret)

    # Het aantal keer dat we geraden hebben
    aantal_gokken = 1

    # Bepaal alle mogelijkheden
    mogelijkheden = PERMUTATIES.copy()

    # Een variabele voor de guess door middel van een keuze menu
    guess = keuze(optie, mogelijkheden)

    # Feedback
    zwart, wit = feedback(secret, guess)

    # Print feedback
    print(f'{guess}: ({zwart},{wit}) poging: {aantal_gokken}')

    # Main game loop
    while secret != guess and aantal_gokken < MAX_GUESSES:

        # Feedback
        zwart, wit = feedback(secret, guess)

        # Bepaal welke mogelijkheden nog over zijn
        mogelijkheden = reduceer(mogelijkheden, guess, (zwart, wit))

        # De guess voor in de while loop
        guess = keuze(optie, mogelijkheden)

        # Feedback
        zwart, wit = feedback(secret, guess)

        # Voeg een poging toe
        aantal_gokken += 1

        # Feedback voor de gebruiker
        print(f'{guess}: ({zwart},{wit}) poging: {aantal_gokken}')

    # Heeft de gebruiker gewonnen?
    if (secret == guess):
        print(f"Je hebt het goed geraden in {aantal_gokken} keer!")
    else:
        print("Sorry! Je hebt de code niet geraden.")

    # Laat de gebruiker opnieuw spelen
    opnieuw()

# Zorg dat het spel alleen runt als we dit specifieke script runnen
if __name__ == "__main__":
    main()


