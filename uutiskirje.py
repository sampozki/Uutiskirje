"""
  _    _       _   _     _  ___      _       _____                                 _   _             _
 | |  | |     | | (_)   | |/ (_)    (_)     / ____|                               | | | |           (_)
 | |  | |_   _| |_ _ ___| ' / _ _ __ _  ___| |  __  ___ _ __   ___ _ __ __ _  __ _| |_| |_ ___  _ __ _
 | |  | | | | | __| / __|  < | | '__| |/ _ \ | |_ |/ _ \ '_ \ / _ \ '__/ _` |/ _` | __| __/ _ \| '__| |
 | |__| | |_| | |_| \__ \ . \| | |  | |  __/ |__| |  __/ | | |  __/ | | (_| | (_| | |_| || (_) | |  | |
  \____/ \__,_|\__|_|___/_|\_\_|_|  | |\___|\_____|\___|_| |_|\___|_|  \__,_|\__,_|\__|\__\___/|_|  |_|
                                   _/ |
                                  |__/
Copyright: sampozki 2018
Tekee uutiskirjeen tiedostosta rungoksi
"""


# Löysin tän Stack overflowsta :3
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
    rivi = str(numero) + " " + otsikko + "\n"

    print(rivi, end="")
    kirjoita(rivi, lang)

    num = 1
    for i in lista:
        rivi = "    " + str(numero) + "." + str(num) + " " + i + "\n"
        print(rivi, end="")
        kirjoita(rivi, lang)
        num += 1

    print()
    kirjoita("\n", lang)


# Generoi lopun rakenteen
def sarake(lista, numero, otsikko, lang):
    otsikkoreuna = "o-----------------------------------------------------------------------o"
    otsikkoreunapieni = "o--------------------------o"
    rivi = otsikkoreunapieni + "\n" + str(numero) + " " + otsikko + "\n" + otsikkoreunapieni + "\n\n"

    print(rivi, end="")
    kirjoita(rivi, lang)

    num = 1
    for i in lista:
        rivi = otsikkoreuna + "\n" + str(numero) + "." + str(num) + " " + i + "\n" + otsikkoreuna + "\n\n\n\n"
        print(rivi, end="")
        kirjoita(rivi, lang)
        num += 1

    kirjoita("\n", lang)


def loppu():
    print("o---------o\nloppu <3\no---------o")
    print("o---------o\nThe End <3\no---------o")

    kirjoita("\n\no---------o\nloppu <3\no---------o\n", "fi")
    kirjoita("\n\no---------o\nThe End <3\no---------o\n", "en")


def kirjoita(rivi, lang):
    if lang == "fi":
        kirjoitustiedosto.write(str(rivi))
    elif lang == "en":
        kirjoitustiedostoen.write(str(rivi))


def main():

    rivit = open("fi.txt", "r", encoding="UTF-8").readlines()
    riviten = open("en.txt", "r", encoding="UTF-8").readlines()

    lista = listaa(rivit)
    listaen = listaa(riviten)

    print(lista, listaen)
    print()

    for a in range(0, 3):
        luettelo(lista[a][1:-1], a + 1, lista[a][0], "fi")
        luettelo(listaen[a][1:-1], a + 1, listaen[a][0], "en")

    for a in range(0, 3):
        sarake(lista[a][1:-1], a + 1, lista[a][0], "fi")
        sarake(listaen[a][1:-1], a + 1, listaen[a][0], "en")

    loppu()


kirjoitustiedosto = open("valmisfi.txt", "w", encoding="UTF-8")
kirjoitustiedostoen = open("valmisen.txt", "w", encoding="UTF-8")

if __name__ == "__main__":
    main()
