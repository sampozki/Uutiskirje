"""
  _    _       _   _     _  ___      _       _____                                 _   _             _
 | |  | |     | | (_)   | |/ (_)    (_)     / ____|                               | | | |           (_)
 | |  | |_   _| |_ _ ___| ' / _ _ __ _  ___| |  __  ___ _ __   ___ _ __ __ _  __ _| |_| |_ ___  _ __ _
 | |  | | | | | __| / __|  < | | '__| |/ _ \ | |_ |/ _ \ '_ \ / _ \ '__/ _` |/ _` | __| __/ _ \| '__| |
 | |__| | |_| | |_| \__ \ . \| | |  | |  __/ |__| |  __/ | | |  __/ | | (_| | (_| | |_| || (_) | |  | |
  \____/ \__,_|\__|_|___/_|\_\_|_|  | |\___|\_____|\___|_| |_|\___|_|  \__,_|\__,_|\__|\__\___/|_|  |_|
                                   _/ |
                                  |__/
Copyright: Sampo 'sampozki' Pelto 2018
Tekee uutiskirjeen tiedostosta rungoksi
"""


# Löysin tän Stack overflowsta :3
# Jakaa tiedostoista tapahtumiksi, uutisiksi jne
def listaa(lista):
    puhdistettulista = []
    for i in lista:
        if i != '':
            puhdistettulista.append(i.rstrip())

    new_biglist = []
    sub_list = []
    for item in puhdistettulista:
        if '*' in item:
            end, start = item.split('*')
            sub_list.append(end)
            new_biglist.append(sub_list)
            sub_list = [start]
        else:
            sub_list.append(item)
    return new_biglist


# Generoi sisällysluettelon
def luettelo(lista, numero, otsikko, lang):
    # Luo sisällyluettelon 1) tapahtumat -sarakkeen
    kirjoita(str(numero) + ") " + otsikko + "\n", lang)

    # Generoi alaotsikot muotoon 1.3 nönnönnöö
    num = 1
    if lista[0] == '':
        if lang == 'fi':
            kirjoita("    /* Ei tiedotettavaa */ \n", lang)
        else:
            kirjoita("    /* Nothing to inform */ \n", lang)
    else:
        for i in lista:
            if i != '':
                rivi = "    " + str(numero) + "." + str(num) + " " + i + "\n"
                kirjoita(rivi, lang)
                num += 1

    # Kirjoittaa valmiiseen tiedostoon
    kirjoita("\n", lang)


# Generoi lopun rakenteen
def uutine(lista, numero, otsikko, lang):
    otsikkoreuna = "o-----------------------------------------------------------------------o"
    otsikkoreunapieni = "o--------------------------o"

    # Tekee tapahtumat jne -otsikon
    kirjoita(otsikkoreunapieni + "\n" + str(numero) + " " + otsikko + "\n" + otsikkoreunapieni + "\n\n", lang)

    # Tekee alaotsikon oikean otsikon alle
    num = 1
    for i in lista:
        if i != '':
            rivi = otsikkoreuna + "\n" + str(numero) + "." + str(num) + " " + i + "\n" + otsikkoreuna + "\n\n\n\n"
            kirjoita(rivi, lang)
            num += 1

    # Kirjoittaa valmiiseen tiedostoon
    kirjoita("\n", lang)


# Generoi uutiskirjeen loppuun tulevan laatikon
def loppu():
    kirjoita("\n\no---------o\nloppu <3\no---------o\n", "fi")
    kirjoita("\n\no---------o\nThe End <3\no---------o\n", "en")


def kirjoita(rivi, lang):
    print(rivi)

    # Kirjottaa oikeaan tiedostoon kielestä riippuen
    if lang == "fi":
        kirjoitustiedosto.write(str(rivi))
    elif lang == "en":
        kirjoitustiedostoen.write(str(rivi))


def main():
    rivit = open("fi.txt", "r", encoding="UTF-8").readlines()
    riviten = open("en.txt", "r", encoding="UTF-8").readlines()

    lista = [listaa(rivit), listaa(riviten)]

    print(lista[0], "\n", lista[1], "\n")

    # Käy läpi kaikki otsikot molemmilla kielillä
    for a in range(0, 3):
        luettelo(lista[0][a][1:-1], a + 1, lista[0][a][0], "fi")
        luettelo(lista[1][a][1:-1], a + 1, lista[1][a][0], "en")

    # Käy läpi kaikki uutiset
    for a in range(0, 3):
        if len(lista[0][a][1:-1]) > 2:
            uutine(lista[0][a][1:-1], a + 1, lista[0][a][0], "fi")
        if len(lista[1][a][1:-1]) > 2:
            uutine(lista[1][a][1:-1], a + 1, lista[1][a][0], "en")

    loppu()


kirjoitustiedosto = open("valmisfi.txt", "w", encoding="UTF-8")
kirjoitustiedostoen = open("valmisen.txt", "w", encoding="UTF-8")

if __name__ == "__main__":
    main()
