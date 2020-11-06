from itertools import zip_longest


def last_index(lst):
    for element in reversed(lst):
        if element != 0:
            return lst.index(element)
    return 0


def wrong_number(number):
    if number is None:
        return 0
    else:
        return number


class Polynomial:

    coefficients = []

    def __str__(self):
        return str(self.coefficients)

    def __bool__(self):
        for coefficients_ in self.coefficients:
            if self.coefficients[coefficients_] != 0:
                return True
        return False

    def __init__(self, coefficients: list):
        coefficients = coefficients[:last_index(coefficients) + 1]
        self.coefficients = coefficients

    def change_coefficients(self, index, value):
        self.coefficients[index] = value

    def evaluate(self, argument):
        result = 0
        power = 0
        for coefficients_ in self.coefficients:
            result += pow(argument, power) * coefficients_
            power += 1
        return result

    def __add__polynomial(self, other):
        coefficients = [wrong_number(a) + wrong_number(b) for a, b in zip_longest(self.coefficients, other.coefficients)]
        return Polynomial(coefficients)
        return result

    def __iadd__(self, other):
        self = self + other
        return self

    def __sub__(self, other):
        coefficients = [wrong_number(a) - wrong_number(b) for a, b in zip_longest(self.coefficients, other.coefficients)]
        return Polynomial(coefficients)

    def __isub__(self, other):
        self = self - other
        return self

    def multiplication_by_value(self, value):
        for coefficients_ in self.coefficients:
            self.coefficients[coefficients_] = value * self.coefficients[coefficients_]

    def __mul__(self, other):

        result = []
        for i in range(0, len(self.coefficients) + len(other.coefficients) - 1):
            result.append(0)
        for i in range(0, len(self.coefficients)):
            for j in range(0, len(other.coefficients)):
                result[i + j] = result[i + j] + self.coefficients[i] * other.coefficients[j]
        return Polynomial(result)

    def __imul__(self, other):
        self = self * other
        return self

