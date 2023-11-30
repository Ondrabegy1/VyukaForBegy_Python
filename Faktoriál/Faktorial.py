#Program pro počítání faktoriálu.

cislo = int(input("Zadej číslo: "))

def faktorial(cislo):
    if cislo == 0:
        return 1
    else:
        return cislo * faktorial(cislo - 1)
    
print(faktorial(cislo))