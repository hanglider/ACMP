from math import factorial
from collections import Counter

with open("input.txt") as f:
    w = f.read().strip()

res = factorial(len(w))
for c in Counter(w).values():
    res //= factorial(c)

print(res)
