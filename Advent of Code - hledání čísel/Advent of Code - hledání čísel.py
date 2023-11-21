#Program pro hledání 3 čísel, která dávají součet 2020 (Advent of Code).

with open("2020.txt", "r") as f:
    cisla = f.read().splitlines()

cisla = [int(i) for i in cisla]

for i in cisla:
    for j in cisla:
        for k in cisla:
            if i + j + k== 2020:
                print(i, j, k)
                print(i * j * k)
                break
        else:
            continue
        break
    else:
        continue
    break