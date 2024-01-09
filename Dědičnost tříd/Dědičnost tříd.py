#Program pro dědičnost tříd s obrazcy.

class Shape:
    def __init__(self):
        print("Vykresluji obrazec")

class Square(Shape):
    def __init__(self, a):
        super().__init__()
        self.a = a
        self.calculate_and_print_square_info()

    def calculate_and_print_square_info(self):
        obsah = self.a ** 2
        obvod = 4 * self.a
        print(f"Obvod ctverce je: {obvod}")
        print(f"Obsah ctverce je: {obsah}")

class Rectangle(Square):
    def __init__(self, a, b):
        super().__init__(a)
        self.calculate_and_print_rectangle_info(b)

    def calculate_and_print_rectangle_info(self, b):
        A = self.a
        obsah = A * b
        obvod = 2 * (A + b)
        print(f"Obvod obdelniku je: {obvod}")
        print(f"Obsah obdelniku je: {obsah}")
        print(f"Strana A je: {A}")
        print(f"Strana B je: {b}")

def main():
    rec = Rectangle(5, 10)

if __name__ == "__main__":
    main()