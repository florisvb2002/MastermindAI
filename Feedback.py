
# Importeer de feedbackfunctie van het internet
# Source: https://github.com/peterstark72/mastermind/blob/master/mastermind.py
def feedback(code, pegs):
    '''
    Returns a tuple with the number of correct guesses (black) and the
    number of correct colors but wrong positions (white)
    :param  tuple   The code, e.g. (1,2,3,4)
    :param  tuple   The guess, e.g. (1,1,1,1)
    :return tuple   The feedback (black, white) or (correct, correct/wrong position)
    Example:
    The code (1,2,3,4) and guess (1,1,1,1), will return (1,0) since only the first peg is correct.
    '''

    # Bepaal een set van alle indices bijv. (0, 1, 2, 3)
    positions = set(range(len(code)))

    # Bepaal de posities waar de pinnen al op de goede plek staan.
    black_positions = set(
        [pos for pos, peg in enumerate(pegs) if peg == code[pos]])
    # Bepaal hoeveel pinnen al goed staan.
    blacks = len(black_positions)

    # Vergelijk de sets met indices om te kijken welke pinnetjes nog over zijn
    remains_pos = positions - black_positions
    # Selecteer de onderdelen van de code die nog over zijn
    remains = [code[pos] for pos in remains_pos]

    # Teller voor correcte kleur/verkeerde positie pinnetjes
    whites = 0
    # Set van kleuren waar al witte pinnetjes voor uitgedeeld zijn
    awarded_duplicates = set()
    # Voor elke index van een overgebleven pin
    for pos in remains_pos:
        # Bepaal de kleur
        color = pegs[pos]
        # Staat de kleur verderop in de code? Én zijn er minder of even veel van deze kleur in
        # de overgebleven code en de geheime code.
        if color in remains and pegs.count(color) <= code.count(color):
            # Voeg een witte pin toe
            whites += 1
        # Als anders de kleur verderop in de code staat en de kleur nog niet in
        elif color in remains and color not in awarded_duplicates:
            # Voeg een witte pin toe
            whites += 1
            # We kunnen verder geen witte pinnen meer toevoegen voor deze kleur
            awarded_duplicates.add(color)

    # Geef het resultaat terug als tuple
    return blacks, whites

# Importeer de freq functie van de les
# Source: https://github.com/LinaBlijlevenHU/StructuredProgramming2023
def freq(lijst):
    '''
    Bepaal hoe vaak een mogelijkheid voorkomt
    :param lijst    lijst van alle mogelijkheden
    :return: dict
    '''
    f = {}

    for element in lijst:
        # Tel 1 op bij de huidige frequentie van het element (default 0)
        f[element] = f.get(element, 0) + 1

    return f


# Importeer de reduceer functie van de les
# Source: https://github.com/LinaBlijlevenHU/StructuredProgramming2023
def reduceer(mogelijkheden, vorige_gok, fb):
    '''
    Bepaal de mogelijkheden die nog over zijn na de laatste gok.
    :param array    Mogelijkheden die er nu nog zijn
    :param tuple    Vorige gok
    :param tuple    Feedback (zwart, wit)
    :return:
    '''
    nieuwe_mogelijkheden = []

    # Test voor elke mogelijkheid of die nog steeds mogelijk is
    for code in mogelijkheden:
        # Bepaal de feedback tussen de vorige gok en de mogelijkheid
        # en vergelijk met de vorige feedback die we hebben gekregen
        if fb == feedback(vorige_gok, code):
            # Code is nog mogelijk
            nieuwe_mogelijkheden.append(code)

    # Geef de nieuwe mogelijkheden terug
    return nieuwe_mogelijkheden




# Worst case scenerio van Groningen Artikel
def worst_case(mogelijkheden):
    '''
    Bepaal de beste code voor het safe spelen
    :param   Mogelijkheden die er zijn
    :return: Beste code
    '''

    # Maak een dictionary aan
    dict_beste = {}

    # Voor elke mogelijk bepaal ik de code en zet ik in een dictionary
    for code in mogelijkheden:

        # Feedback functie gebruiken voor elke code
        feedback1 = [feedback(combi, list(code)) for combi in mogelijkheden]

        # Functie freq gebruiken om te kijken hoe vaak een mogelijkheid voorkomt
        alle_freq = freq(feedback1)

        # Bepaal de max value van elke mogelijkheid
        max_value = max(alle_freq.values())

        # Zet de code en de max value in de gemaakte dictionary
        dict_beste[code] = max_value

        # De safest code is code met de minste mogelijkheden
        beste_code = min(dict_beste, key=dict_beste.get)

    # return de beste code
    return beste_code

# Expected case scenerio van Groningen Artikel
def expected_case(mogelijkheden):
    '''
    Bepaal de beste code door middel van de beste optie
    :param     Mogelijkheden die er zijn
    :return:   Beste code
    '''

    # Maak een dictionary aan
    dict_beste = {}


    # Voor elke mogelijk bepaal ik de code en zet ik in een dictionary
    for code in mogelijkheden:

        # Feedback functie gebruiken voor elke code
        feedback1 = [feedback(combi, list(code)) for combi in mogelijkheden]

        # Functie freq gebruiken om te kijken hoe vaak een mogelijkheid voorkomt
        alle_freq = freq(feedback1)

        # Maak een lijst aan voor addup
        addup = []

        # Voor elke value van de freq van de bijbehorende code
        for x in alle_freq.values():

            # Formule voor het gemiddelde van de freq van de code
            formule = (x / len(mogelijkheden)) * x

            # Append de formule naar de lijst
            addup.append(formule)

            # De som van de lijst
            som = sum(addup)

            # De code en som aan de dictionary toevoegen
            dict_beste[code] = som

            # Beste code is de code met de laagste som dus hierbij de
            beste_code = min(dict_beste, key=dict_beste.get)

    # return beste code
    return beste_code

# Dit is een creatief algoritme die ik heb bedacht door middel van de worst case scenario
# Omdat de worst case scenario de beste optie keus heb ik het omgedraaid
# Dit heb ik gedaan om nu de hoogste value te pakken met de meeste mogelijkheden
# Dit algoritme heet dumb case omdat hij dus de slechtste keus maakt
# Maar dit algoritme is nog steeds slimmer dan de meeste mensen omdat die nog wel alle mogelijkheden onthoud na de slechtste keuze


# Ook hier is gebruik gemaakt van het Groningen Artikel
def dumb_case(mogelijkheden):
    '''
    Bepaal de beste code voor het safe spelen
    :param   Mogelijkheden die er zijn
    :return: Beste code
    '''

    # Maak een dictionary aan
    dict_beste = {}

    # Voor elke mogelijk bepaal ik de code en zet ik in een dictionary
    for code in mogelijkheden:

        # Feedback functie gebruiken voor elke code
        feedback1 = [feedback(combi, list(code)) for combi in mogelijkheden]

        # Functie freq gebruiken om te kijken hoe vaak een mogelijkheid voorkomt
        alle_freq = freq(feedback1)

        # Bepaal de max value van elke mogelijkheid
        max_value = max(alle_freq.values())

        # Zet de code en de max value in de gemaakte dictionary
        dict_beste[code] = max_value

        # Nu kijk ik dus naar de max value en dat is de slechtste code
        slechtste_code = max(dict_beste, key=dict_beste.get)

    # Return de slechtste code
    return slechtste_code






