a, b, c, d = map(int, input().split())
n = a * c + 1
if a < 2:
    n = max(n, d + 1)
if c < 2:
    n = max(n, b + 1)
while min(a, c) < 2 and any(n % u < 1 and (a <= u <= b and c <= n // u <= d or a <= n // u <= b and c <= u <= d) for u in range(1, int(n**.5) + 1)):
    n += 1
print(n)
