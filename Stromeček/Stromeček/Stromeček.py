#Program pro vytvo�en� strome�ku.

def Stromecek(vyska_koruny, vyska_kmene, sirka_kmene):
        
    if vyska_kmene > vyska_koruny:
        print("Koruna mus� b�t v�t�� ne� kmen.")
        
    else:
        for i in range(vyska_koruny):
            print(" " * (vyska_koruny - i - 1) + "*" * (i * 2 + 1))
        for i in range(vyska_kmene):
            print(" " * (vyska_koruny - sirka_kmene // 2 - 1) + "*" * sirka_kmene)
            
vyska_koruny = int(input("Zadejte v��ku koruny: "))
vyska_kmene = int(input("Zadejte v��ku kmene: "))
sirka_kmene = int(input("Zadejte ���ku kmene: "))

if sirka_kmene % 2 == 0:
        print("���ka kmene mus� b�t lich� ��slo.")
        
else:
    Stromecek(vyska_koruny, vyska_kmene, sirka_kmene) 