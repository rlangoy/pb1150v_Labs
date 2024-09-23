# Base class to hold two numbers
class Numbers:
    def __init__(self, a, b):
        self._a = a  # Protected variable
        self._b = b  # Protected variable

# Class for addition operation
class Addition(Numbers):
    def add(self):
        return self._a + self._b

# Class for subtraction operation
class Subtraction(Numbers):
    def subtract(self):
        return self._a - self._b

# Class for multiplication operation
class Multiplication(Numbers):
    def multiply(self):
        return self._a * self._b

# Class for division operation
class Division(Numbers):
    def divide(self):
        if self._b != 0:
            return self._a / self._b
        else:
            return "Error: Division by zero"

# Class for power (exponentiation) operation
class Power(Numbers):
    def power(self):
        return self._a ** self._b

# Class for modulus operation
class Modulus(Numbers):
    def modulus(self):
        return self._a % self._b

# Calculator class inheriting from all operation classes
class Calculator(Addition, Subtraction, Multiplication, Division, Power, Modulus):
    def __init__(self, a, b):
        Numbers.__init__(self, a, b)  # Initialize Numbers class

# Example usage
if __name__ == "__main__":
    calc = Calculator(10, 5)

    # Operations
    print("Addition:", calc.add())
    print("Subtraction:", calc.subtract())
    print("Multiplication:", calc.multiply())
    print("Division:", calc.divide())
    print("Power:", calc.power())
    print("Modulus:", calc.modulus())


