import math
N, K1, K2, S = map(int, input().split())
S = int(S)
a = N - K1
b = N - K2
n = a + b - 1
c = sum(math.comb(n, i) for i in range(b))
p = S * c
d = 2 ** n
x = p // d
print(x, S - x)
