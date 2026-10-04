from math import isqrt
for k in map(int, open(0).read().split()[1:]):
    a = (k + isqrt(5 * k * k)) // 2
    print(a, a + k)
