# Importeer de geldige gok functie van de les
# Source: https://github.com/LinaBlijlevenHU/StructuredProgramming2023

def geldige_gok(guess):
    '''
    Bepaal of de gok geldig is
    :param  None|string
    :return boolean
    '''
    # Hebben we een gok van de juiste lengte?
    if (guess == None):
        return False

    if (len(guess) != LENGTE):
        print("Je code heeft niet de juiste lengte.")
        return False

    # Bevat de gok alleen kleuren die voor mogen komen?
    for pin in guess:
        # Als de kleur niet in de toegestane kleuren zit, weten we al dat de code ongeldig is.
        if pin not in KLEUREN:
            print(f"De kleur {pin} is niet geldig. Je kunt kiezen uit {KLEUREN}.")
            return False

    # Alles in orde, de gok is geldig
    return True


# Importeer de vraag input functie van de les
# Source: https://github.com/LinaBlijlevenHU/StructuredProgramming2023
def vraag_input():
    '''
    Vraag de gebruiker om input
    :return:    tuple  De geraden code
    '''
    # We beginnen met een lege gok
    guess = None

    # We vragen codes tot we een geldige gok hebben
    while not geldige_gok(guess):
        print(f"Je kan kiezen uit de volgende kleuren: {KLEUREN}")
        user_input = input(f"Raad een code (bijv. {VOORBEELDCODE}): ")

        # Zet de gok om naar een tuple
        guess = tuple(list(user_input))

    return guess


