from math import *
from collections import *
n, *a = map(int, open(0).read().split())
print(max(Counter((x // gcd(x, y), y // gcd(x, y)) for x, y in zip(a[::2], a[1::2])).values()))
