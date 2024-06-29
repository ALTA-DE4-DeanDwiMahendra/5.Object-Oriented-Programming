# tulis solusi code disini
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a // b  # Pembagian menghasilkan hasil integer

def main():
    calculator = Calculator()

    print("Kalkulator")
    print(f"Penjumlahan (3, 4): {calculator.add(3, 4)}")
    print(f"Pengurangan (15, 4): {calculator.subtract(15, 4)}")
    print(f"Perkalian (10, 10): {calculator.multiply(10, 10)}")
    print(f"Pembagian (12, 3): {calculator.divide(12, 3)}")

if __name__ == "__main__":
    main()
