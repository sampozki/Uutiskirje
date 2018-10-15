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


def sarake(lista, numero, otsikko):
    num = 1
    otsikkoreuna = "o-----------------------------------------------------------------------o"
    otsikkoreunapieni = "o--------------------------o"

    rivi = otsikkoreunapieni + "\n" + str(numero) + " " + otsikko + "\n" + otsikkoreunapieni + "\n\n"
    print(rivi)
    kirjoita(rivi)

    for i in lista:
        rivi = otsikkoreuna + "\n" + str(numero) + "." + str(num) + " " + i + "\n" + otsikkoreuna + "\n\n\n\n"
        print(rivi)
        kirjoita(rivi)
        num += 1
    kirjoita("\n")


def sarakeen(lista, numero, otsikko):
    num = 1
    otsikkoreuna = "o-----------------------------------------------------------------------o"
    otsikkoreunapieni = "o--------------------------o"

    print(otsikkoreunapieni + "\n" + str(numero) + " " + otsikko + "\n" + otsikkoreunapieni + "\n")
    kirjoitaen(otsikkoreunapieni + "\n" + str(numero) + " " + otsikko + "\n" + otsikkoreunapieni + "\n\n")

    for i in lista:
        print(otsikkoreuna + "\n" + str(numero) + "." + str(num) + " " + i + "\n" + otsikkoreuna + "\n\n\n")
        kirjoitaen(otsikkoreuna + "\n" + str(numero) + "." + str(num) + " " + i + "\n" + otsikkoreuna + "\n\n\n\n")
        num += 1
    kirjoitaen("\n")


def luettelo(lista, numero, otsikko):
    num = 1
    print(str(numero) + " " + otsikko)
    kirjoita(str(numero) + " " + otsikko + "\n")

    for i in lista:
        print("    " + str(numero) + "." + str(num) + " " + i)
        kirjoita("    " + str(numero) + "." + str(num) + " " + i + "\n")
        num += 1
    print()
    kirjoita("\n")


def luetteloen(lista, numero, otsikko):
    num = 1
    print(str(numero) + " " + otsikko)
    kirjoitaen(str(numero) + " " + otsikko + "\n")

    for i in lista:
        print("    " + str(numero) + "." + str(num) + " " + i)
        kirjoitaen("    " + str(numero) + "." + str(num) + " " + i + "\n")
        num += 1
    print()
    kirjoitaen("\n")


def loppu():
    print("o---------o\nloppu <3\no---------o")
    print("o---------o\nThe End <3\no---------o")

    kirjoita("\n\no---------o\nloppu <3\no---------o\n")
    kirjoitaen("\n\no---------o\nThe End <3\no---------o\n")


def kirjoita(rivi):
    kirjoitustiedosto.write(str(rivi))


def kirjoitaen(rivi):
    kirjoitustiedostoen.write(str(rivi))


def main():

    fipohja = open("fi.txt", "r", encoding="UTF-8")
    enpohja = open("en.txt", "r", encoding="UTF-8")

    rivit = fipohja.readlines()
    riviten = enpohja.readlines()

    lista = listaa(rivit)
    listaen = listaa(riviten)

    print(lista)
    print(listaen)
    print()

    for a in range(0, 3):
        luettelo(lista[a][1:-1], a + 1, lista[a][0])
        luetteloen(listaen[a][1:-1], a + 1, listaen[a][0])

    for a in range(0, 3):
        sarake(lista[a][1:-1], a + 1, lista[a][0])
        sarakeen(listaen[a][1:-1], a + 1, listaen[a][0])

    loppu()


kirjoitustiedosto = open("valmisfi.txt", "w", encoding="UTF-8")
kirjoitustiedostoen = open("valmisen.txt", "w", encoding="UTF-8")
main()
