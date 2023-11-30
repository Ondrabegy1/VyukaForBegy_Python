#Program pro list množení ryb.

from os. path import realpath, dirname, join
from collections import deque

def play(Ryba:list[int], pocet_tahu:int) -> int:
    Ryba = deque(Ryba)
    for t in range(pocet_tahu):
        Ryba.rotate(-1)
        Ryba[6]+=Ryba[-1]
        #print(Ryba)
    return sum(Ryba)

with open (join(dirname(realpath(__file__)), "input.txt"), "r", encoding = 'utf_8') as file:
    data = [0]*9
    for Ryba in file. read().split(','):
        data[int(Ryba)] += 1

    print(play(data, 256))