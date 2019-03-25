def gcd(m, n):
    while n:
        m, n = n, m % n
    return m


class Fraction:
    """Fractional numbers and their relevant operations"""
    def __init__(self, num, denom):
        if denom < 0:
            self.num = -num
            self.denom = -denom
        elif denom == 0:
            print('You cannot assign Negative Number on Denominator')
            exit(0)
        else:
            self.num = num
            self.denom = denom

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        newNum = self.num * other.denom + self.denom * other.num
        newDenom = self.denom * other.denom
        common = gcd(newNum, newDenom)
        return Fraction(newNum//common, newDenom//common)

    def __sub__(self, other):
        newNum = self.num * other.denom - self.denom * other.num
        newDenom = self.denom * other.denom
        common = gcd(newNum, newDenom)
        return Fraction(newNum // common, newDenom // common)

    def __mul__(self, other):
        newNum = self.num * other.num
        newDenom = self.denom * other.denom
        common = gcd(newNum, newDenom)
        return Fraction(newNum // common, newDenom // common)

    def __truediv__(self, other):
        newNum = self.num * other.denom
        newDenom = self.denom * other.num
        common = gcd(newNum,newDenom)
        return Fraction(newNum // common, newDenom // common)

    # Add more arithmetic operators here such as -, *, /.

    def __eq__(self, other):
        return (self.num * other.denom) == (other.num * self.denom)

    def __lt__(self, other):
        return self.num * other.denom < self.denom * other.num

    def __le__(self, other):
        return self.num * other.denom <= self.denom * other.num

    def __ge__(self, other):
        return self.num * other.denom >= self.denom * other.num

    def __gt__(self, other):
        return self.num * other.denom > self.denom * other.num

    def __ne__(self, other):
        return (self.num * other.denom) != (other.num * self.denom)
    # Add more comparison operators here such as !=, <, <=, >, >=.


if __name__ == "__main__":
    # You can test your implementation here as followings

    my_fraction = Fraction(3, -5)
    print(f"Fraction(3,5) will be represented as {my_fraction}.")
    print(f"I ate {my_fraction} of the pizza.")

    f1 = Fraction(1, 2)
    f2 = Fraction(1, 2)
    print(f"{f1} >= {f2} = {f1 >= f2}")

    f1 = Fraction(1, 2)
    f2 = f1
    print(f"Is f1 identical to f2? {f1 is f2}")
    print(f"Is f1 equal to f2? {f1 == f2}")

    f2 = Fraction(1, 2)
    print(f"Is f1 identical to f2? {f1 is f2}")
    print(f"Is f1 equal to f2? {f1 == f2}")
    help(Fraction)
    # Test codes for various operators of fraction numbers