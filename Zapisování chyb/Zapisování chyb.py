#Program ve kterém budeme počítat a při chybě provedeme zápis do souboru.

import re
import requests

def pocitani():
    cislo1 = input("Zadej první číslo: ")
    cislo2 = input("Zadej druhé číslo: ")

    try:
        cislo1 = int(cislo1)
        cislo2 = int(cislo2)
        vysledek = cislo1 / cislo2
        print("Výsledek je: ", vysledek)
    except ValueError:
        print("Nezadal jsi číslo")
        with open("chyby.txt", "a", encoding = "utf-8") as soubor:
            soubor.write("Nezadal jsi číslo.\n")
        pocitani()
    except ZeroDivisionError:
        print("Nemůžeš dělit nulou")
        with open("chyby.txt", "a", encoding = "utf-8") as soubor:
            soubor.write("Nemůžeš dělit nulou.\n")
        pocitani()

pocitani()