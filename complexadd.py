class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)


print("Enter real and imaginary part of complex No - 1(separated by space)")
A = complex(*map(float, input().strip().split()))
print("Enter real and imaginary part of complex No - 2(separated by space)")
B = complex(*map(float, input().strip().split()))

print(f"Sum of numbers : {str(A + B)}")