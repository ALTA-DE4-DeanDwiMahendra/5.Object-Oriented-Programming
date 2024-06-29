# tulis solusi code disini
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        # Assuming an equilateral triangle for simplicity
        return 3 * self.base

def main():
    print("Luas")
    square = Square(4)
    print(f"Persegi: {square.area()}")

    triangle = Triangle(3, 4)
    print(f"Segitiga: {triangle.area()}")

    rectangle = Rectangle(7, 8)
    print(f"Persegi Panjang: {rectangle.area()}")

    print("\nKeliling")
    print(f"Persegi: {square.perimeter()}")
    print(f"Segitiga: {triangle.perimeter()}")
    print(f"Persegi Panjang: {rectangle.perimeter()}")

if __name__ == "__main__":
    main()