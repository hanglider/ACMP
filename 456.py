x, y = map(int, open('input.txt').read().split())

c, d = 1, 1
for _ in range(x - 3):
    c, d = d, c + d

for b in range(y + 1):
    a, r = divmod(y - b * d, c)
    if r == 0 and a > b:
        print(a, b)
        break
