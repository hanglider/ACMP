from math import *
n, k, *s = open(0).read().split()
for i in sorted(range(int(n)), key=lambda i: atan2(1 - float(s[2 * i]), int(s[2 * i + 1]))):
    print(i + 1)
