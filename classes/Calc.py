#create class to calculate the sum of numbers and return the result in json format
class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2