#Simple Calculator
"""
Project Idea: Create a basic calculator that can perform addition, subtraction, multiplication,
and division operations.Each operation can be implemented as a separate class.
Why It’s Great for Beginners: This project demonstrates how to create multiple classes that work
together to perform different tasks.
"""

class Adder:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 + self.num2


class Subtractor:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 - self.num2


class Multiplier:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 * self.num2


class Divisor:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        if self.num2 == 0:
            return "Error"
        else:
            return self.num1 / self.num2

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

operation = input("Enter operation: +,-,*,/ ")
if operation == "+":
    add = Adder(first_num, second_num)
    print(add.calculate())
elif operation == "-":
    sub = Subtractor(first_num, second_num)
    print(sub.calculate())
elif operation == "*":
    mul = Multiplier(first_num, second_num)
    print(mul.calculate())
elif operation == "/":
    div = Divisor(first_num, second_num)
    print(div.calculate())
else:
    print("Invalid operation")