n, *s = open(0).read().split()
f = 0
r = []
for i in range(0, len(s), 5):
    a, b, c, d = map(int, s[i + 1:i + 5])
    r += [f - b + c if s[i] < 'L' else -1]
    f += c + d - a - b
print(*r)
