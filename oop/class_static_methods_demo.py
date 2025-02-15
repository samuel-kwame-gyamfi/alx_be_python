class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b

    # Class method to multiply two numbers and print the calculation type
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
