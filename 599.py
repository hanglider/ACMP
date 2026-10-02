from itertools import*
n = int(input())
s = [ord(c) - 97 for c in input().split()]
W = [sum(abs(c - x) << 40 * c for c in range(26)) for x in range(26)]
w = [W[x] for x in s]
p = n // 2
q = n - p
d = lambda k: min(k % n, -k % n)
a = sum(w[j] * d(j) for j in range(n))
b = sum(w[j] * d(1 - j) for j in range(n))
g = accumulate(chain([b - a], (2 * w[i] - w[i - p] - w[i - q] for i in range(1, n - 1))))
m, i = max(zip((f >> 40 * x & 2**40 - 1 for f, x in zip(accumulate(g, initial=a), s)), count(1)))
print(m)
print(i)
