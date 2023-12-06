#Program pro výpočet vzdálenosti lodi od počátku. Loď je naváděna pomocí waypointu.

from os.path import dirname, join, realpath

class Lod:
    __sever:int = 0
    __vychod:int = 0
    _stupne:int = 90
    __waypoint:tuple[int, int] = (1, 10)

    def __init__(self, sever:int, vychod:int, stupne:int, waypoint:tuple[int, int]) -> None:
        self.__sever = sever
        self.__vychod = vychod
        self._stupne = stupne
        self.__waypoint = waypoint

    def __repr__(self) -> str:
        return f"Severni souradnice: {self.__sever}\nVychodni souradnice: {self.__vychod}\nVzdálenost: {abs(self.__sever) + abs(self.__vychod)}"
    
    def rotace_waypointu(self, smer:str, stupne:int) -> None:
        if smer == "L":
            stupne = 360 - stupne
        if smer == "R":
            stupne = stupne

        if stupne == 90:
            self.__waypoint = (self.__waypoint[1], -self.__waypoint[0])
        elif stupne == 180:
            self.__waypoint = (-self.__waypoint[0], -self.__waypoint[1])
        elif stupne == 270:
            self.__waypoint = (-self.__waypoint[1], self.__waypoint[0])

    def pohyb_waypointu(self, smer:str, vzdalenost:int) -> None:
        if smer == "N":
                    self.__waypoint = (self.__waypoint[0] + vzdalenost, self.__waypoint[1])
        elif smer == "S":
                    self.__waypoint = (self.__waypoint[0] - vzdalenost, self.__waypoint[1])
        elif smer == "E":
                    self.__waypoint = (self.__waypoint[0], self.__waypoint[1] + vzdalenost)
        elif smer == "W":
                    self.__waypoint = (self.__waypoint[0], self.__waypoint[1] - vzdalenost)

    def pohyb_lodi(self, smer:str, vzdalenost:int) -> None:
        if smer == "F":
            self.__sever += vzdalenost * self.__waypoint[0]
            self.__vychod += vzdalenost * self.__waypoint[1]
              
    
    def Naviguj(self, soubor:str) -> None:
        with open(join(dirname(realpath(__file__)), soubor), 'r', encoding='utf-8') as file:
            for line in file.read().split('\n'):
                self.pohyb_lodi(line[0], int(line[1:]))

def main():
    novaLod = Lod(0,0,90,(1,10))
    novaLod.Naviguj("input.txt")
    print(novaLod)

if __name__ == "__main__":
    main()