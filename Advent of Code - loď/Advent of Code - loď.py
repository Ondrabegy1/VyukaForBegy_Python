#Program pro výpočet vzdálenosti lodi od počátku.

from os.path import dirname, join, realpath

class Lod:
    __sever:int = 0
    __vychod:int = 0
    __stupne:int = 90

    def __init__(self, sever:int, vychod:int, stupne:int) -> None:
        self.__sever = sever
        self.__vychod = vychod
        self.__stupne = stupne

    def __repr__(self) -> str:
        return f"Severni souradnice: {self.__sever}\nVychodni souradnice: {self.__vychod}\nStupne: {self.__stupne}\nVzdálenost: {abs(self.__sever) + abs(self.__vychod)}"
    
    def Pohyb(self, smer:str, hodnota:int) -> None:
        match smer:
            case 'N':
                self.__sever += hodnota
            case 'S':
                self.__sever -= hodnota
            case 'E':
                self.__vychod += hodnota
            case 'W':
                self.__vychod -= hodnota
            case 'L':
                self.Rotace(smer, hodnota)
            case 'R':
                self.Rotace(smer, hodnota)
            case 'F':
                match self.__stupne:
                    case 0:
                        self.__sever += hodnota
                    case 90:
                        self.__vychod += hodnota
                    case 180:
                        self.__sever -= hodnota
                    case 270:
                        self.__vychod -= hodnota
                    case _:
                        pass
            case _:
                pass

    def Rotace(self, smer:str, hodnota:int) -> None:
        if smer == 'L':
            self.__stupne -= hodnota
        elif smer == 'R':
            self.__stupne += hodnota
        else:
            pass

        if self.__stupne < 0:
            self.__stupne += 360
        elif self.__stupne >= 360:
            self.__stupne -= 360
        else:
            pass

    def Naviguj(self, soubor:str) -> None:
        with open(join(dirname(realpath(__file__)), soubor), 'r', encoding='utf-8') as file:
            for line in file.read().split('\n'):
                self.Pohyb(line[0], int(line[1:]))

def main():
    novaLod = Lod(0,0,90)
    novaLod.Naviguj("input.txt")
    print(novaLod)

if __name__ == "__main__":
    main()