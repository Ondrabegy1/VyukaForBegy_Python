#Program pro překlad textu do Morseovy abecedy.

from os.path import dirname, join, realpath

d = {}

def main():

    vysledek = str()

    with open(join(dirname(realpath(__file__)), "input.txt"), "r") as f:
        data = f.read()
        data = data.split("\n")
        
        for radek in data:
            d[radek[0]] = radek[2:]

    data = input("Zadejte text: ")
    data = data.upper()

    for znak in data:
        if znak in d:
            vysledek += d[znak]
        else:
            print("Znak neexistuje")

    print(vysledek)

main()

