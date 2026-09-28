from math import comb
n = int(input())
l = 1
while n > comb(l + 8, 8):
    n -= comb(l + 8, 8)
    l += 1
s = ""
c = 1
for r in range(l - 1, -1, -1):
    while n > comb(r + 9 - c, r):
        n -= comb(r + 9 - c, r)
        c += 1
    s += str(c)
print(s)
