# tulis solusi code disini
import math

class Solid:
    def volume(self):
        pass

class Cube(Solid):
    def __init__(self, side):
        self.side = side

    def volume(self):
        return self.side ** 3

class RectangularPrism(Solid):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

class Cylinder(Solid):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

def main():
    print("Volume")
    cube = Cube(10)
    print(f"Kubus: {cube.volume()}")

    rectangular_prism = RectangularPrism(3, 6, 10)
    print(f"Balok: {rectangular_prism.volume()}")

    cylinder = Cylinder(7, 10)
    print(f"Tabung: {int(cylinder.volume())}")  # Pembulatan ke integer untuk output sesuai contoh

if __name__ == "__main__":
    main()