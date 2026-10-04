a, b = open(0).read().split()
m = len(b)
q = 2**61 - 1
w = pow(131, m, q)
r = []
for s in b + b[:-1], a:
    h = [0]
    for c in s:
        h += [(h[-1] * 131 + ord(c)) % q]
    r += [[(h[i + m] - h[i] * w) % q for i in range(len(s) - m + 1)]]
print(sum(map(set(r[0]).__contains__, r[1])))
