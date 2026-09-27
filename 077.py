from math import comb
n, k = map(int, input().split())
b = f"{n:b}"
l = len(b)
r = z = 0
for i in range(1, l):
    r += comb(i - 1, k) + (b[i] > "0" and k > z and comb(l - i - 1, k - z - 1))
    z += b[i] < "1"
print(r + (b.count("0") == k))
