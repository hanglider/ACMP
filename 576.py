from math import gcd
n = int(open('input.txt').read())
print(sum(gcd(i, n) < 2 for i in range(1, n)))