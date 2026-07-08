x = int(input())
s = [True] * (x + 1)
s[0] = s[1] = False
for i in range(2, int(x**0.5) + 1):
    if s[i]:
        for j in range(i * i, x + 1, i):
            s[j] = False
c = 0
for p in range(2, x // 2 + 1):
    if s[p] and p <= x - p and s[x - p]:
        c += 1
print(c)
