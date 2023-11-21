#Program pro vytvoøení stromeèku.

def Stromecek(vyska_koruny, vyska_kmene, sirka_kmene):
        
    if vyska_kmene > vyska_koruny:
        print("Koruna musí bıt vìtší ne kmen.")
        
    else:
        for i in range(vyska_koruny):
            print(" " * (vyska_koruny - i - 1) + "*" * (i * 2 + 1))
        for i in range(vyska_kmene):
            print(" " * (vyska_koruny - sirka_kmene // 2 - 1) + "*" * sirka_kmene)
            
vyska_koruny = int(input("Zadejte vıšku koruny: "))
vyska_kmene = int(input("Zadejte vıšku kmene: "))
sirka_kmene = int(input("Zadejte šíøku kmene: "))

if sirka_kmene % 2 == 0:
        print("Šíøka kmene musí bıt liché èíslo.")
        
else:
    Stromecek(vyska_koruny, vyska_kmene, sirka_kmene) 