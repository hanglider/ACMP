s, n = map(int, open('input.txt').read().split())
c, d, o = n - s + 1, 1, 1
while c > 1:
    s += d * o
    c = (c + 1 - o) // 2
    d *= 2
    o ^= 1
print(s)
