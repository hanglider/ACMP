k, a, b, c = map(int, open(0).read().split())
v = 100 - 2 * b
e = 2 * a + c - 100 - v
q = e and -k * v // e
print(min((abs(k * v + x * e), x) for x in {min(max(y, 1), k - 1) for y in (q, q + 1)})[1])
