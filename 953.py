from fractions import Fraction

m, n = map(int, input().split())
rest = Fraction(m, n)
denominators = []
# Greedy: the smallest possible next denominator always leaves a representable remainder
while rest > 0:
    x = -(-rest.denominator // rest.numerator)
    denominators.append(x)
    rest -= Fraction(1, x)
print(' '.join(map(str, denominators)))
