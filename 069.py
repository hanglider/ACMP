from math import *
n, a = map(int, input().split())
print("YNEOS"[a * tan(pi / 2 / n) > 2::2])
