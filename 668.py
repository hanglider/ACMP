n, m = map(int, input().split())
r = -1
for t in range(4 * (m > 0)):
    if (m + t) % 2 == 0 and (n + (m + t) // 2) % 2 == 0:
        r = t + (m + t) // 2 + (n + (m + t) // 2) // 2
        break
if m == 0 and n % 2 == 0:
    r = n // 2
print(r)
