class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = ComplexNumber(2, 9)
c2 = ComplexNumber(4, 5)
print("Sum:", c1 + c2)
print("Difference:", c1 - c2) 
