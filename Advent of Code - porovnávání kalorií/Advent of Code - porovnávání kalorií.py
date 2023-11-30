#Program pro porovnávání kalorií u elfů a vybrání nejvíce kalorií.

with open("input.txt", "r", encoding = "utf_8") as f:
    seznam = f.read().split("\n\n")
    seznam = [x.split("\n") for x in seznam]
    seznam = [[int(x) for x in y] for y in seznam]
    seznam = [sum(x) for x in seznam]
    print(max(seznam))

#Druhá část, která vypíše tři největší počty kalorií a jejich součet.

with open("input.txt", "r", encoding = "utf_8") as f:
    seznam = f.read().split("\n\n")
    seznam = [x.split("\n") for x in seznam]
    seznam = [[int(x) for x in y] for y in seznam]
    seznam = [sum(x) for x in seznam]
    print(sorted(seznam)[-3:])
    print(sum(sorted(seznam)[-3:]))