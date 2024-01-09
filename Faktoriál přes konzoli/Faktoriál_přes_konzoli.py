#Program pro vypočítání faktoriálu a mocnění přes konzolové příkazy.

import argparse

parser = argparse.ArgumentParser(description='Program pro výpočet faktoriálu a mocnění přes konzolové příkazy.')
parser.add_argument('-c', metavar='--cislo',type=int, help='Zadejte číslo, které chcete umocnit nebo z něj vypočítat faktoriál.')
parser.add_argument('-p', metavar='--pocet', type=int, help='Zadejte počet opakování mocnin.')
parser.add_argument('-f', metavar='--faktorial', action=argparse.BooleanOptionalAction, help='Vypočítá faktoriál zadaného čísla.')
parser.add_argument('-m', metavar='--mocnina', type=int, action=argparse.BooleanOptionalAction, help='Vypočítá mocninu zadaného čísla.')

args = parser.parse_args()

if args.f:
    cislo = args.c
    faktorial = 1
    for i in range(1, cislo + 1):
        faktorial = faktorial * i
    print(faktorial)

elif args.m:
    cislo = args.c
    pocet = args.p
    vysledek = cislo ** pocet
    print(vysledek)

else:
    print('Zadejte příkaz -f nebo -m.')