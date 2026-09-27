I = input
d = [0] * 2400
for _ in range(int(I())):
    a, b = I().replace(":", "").split()
    d[int(a)] += 1
    d[int(b) + 1] -= 1
c = r = 0
for x in d:
    c += x
    r = max(r, c)
print(r)
