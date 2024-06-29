# tulis solusi code disini
class Shipment:
    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    def calculate_volume(self):
        return self.length * self.width * self.height

    def calculate_cost(self):
        volume = self.calculate_volume()
        if volume >= 50:
            return 5000
        else:
            return 0  # Misalnya tidak dikenakan biaya jika kurang dari 50 cm3

def main():
    length = 5
    width = 2
    height = 4
    weight = 1

    shipment = Shipment(length, width, height, weight)
    cost = shipment.calculate_cost()

    print(f"Panjang = {length}")
    print(f"Lebar = {width}")
    print(f"Tinggi = {height}")
    print(f"Berat = {weight} kg")
    print(f"Harga: Rp {cost}")

if __name__ == "__main__":
    main()
