#Program pro dědičnost tříd s obrazcy.

import math

class Shape:
    def __init__(self):
        print("Vykresluji obrazec")

class Square(Shape):
    def __init__(self, a=0):
        super().__init__()
        self.a = a
        obsah = round(a * a, 2)
        obvod = round(4 * a, 2)
        print(f"Obvod čtverce je: {obvod}")
        print(f"Obsah čtverce je: {obsah}")
        print(f"Strana A je: {a}")

class Rectangle(Square):
    def __init__(self, a=0, b=0):
        super().__init__(a)
        self.b = b
        obsah = round(self.a * b, 2)
        obvod = round(2 * (self.a + b), 2)
        print(f"Obvod obdélníku je: {obvod}")
        print(f"Obsah obdélníku je: {obsah}")
        print(f"Strana A je: {self.a}")
        print(f"Strana B je: {b}")

class Circle(Square):
    def __init__(self, a=0):
        super().__init__(a)
        r = self.a
        obsah = round(math.pi * (r * r), 2)
        obvod = round(2 * math.pi * r, 2)
        print(f"Obvod kruhu je: {obvod}")
        print(f"Obsah kruhu je: {obsah}")
        print(f"Poloměr je: {r}")

class Cube(Square):
    def __init__(self, a=0):
        super().__init__(a)
        obsah = round(6 * (self.a * self.a), 2)
        objem = round(self.a * self.a * self.a, 2)
        print(f"Objem krychle je: {objem}")
        print(f"Obsah krychle je: {obsah}")
        print(f"Strana A je: {self.a}")

class Cuboid(Square):
    def __init__(self, a=0, b=0, c=0):
        super().__init__(a)
        obsah = round(2 * (self.a * b + self.a * c + b * c), 2)
        objem = round(self.a * b * c, 2)
        print(f"Objem kvádru je: {objem}")
        print(f"Obsah kvádru je: {obsah}")
        print(f"Strana A je: {self.a}")
        print(f"Strana B je: {b}")
        print(f"Strana C je: {c}")

class Sphere(Square):
    def __init__(self, a=0):
        super().__init__(a)
        r = self.a
        obsah = round(4 * math.pi * (r * r), 2)
        objem = round((4 / 3) * math.pi * (r * r * r), 2)
        print(f"Objem koule je: {objem}")
        print(f"Obsah koule je: {obsah}")
        print(f"Poloměr je: {r}")

class Cylinder(Square):
    def __init__(self, a=0, b=0):
        super().__init__(a)
        r = self.a
        obsah = round(2 * math.pi * r * (r + b), 2)
        objem = round(math.pi * (r * r) * b, 2)
        print(f"Objem válce je: {objem}")
        print(f"Obsah válce je: {obsah}")
        print(f"Poloměr je: {r}")
        print(f"Výška je: {b}")

if __name__ == "__main__":
    rec = Rectangle(5, 10)
    print()

    cir = Circle(5)
    print()

    cyl = Cylinder(5, 10)