n, q = input().split()
n = int(n)
Q = round(float(q) * 1000)
ok = True
for _ in range(n):
    a, b, c, d = map(int, input().split())
    if (c * c + d * d) * 1000000 > Q * Q * (a * a + b * b):
        ok = False
print("Yes" if ok else "No")
