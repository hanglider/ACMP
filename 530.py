w, h, *s = open(0).read().split()
h = int(h)
o = ''.join(s[2 * h:])
for i in range(h):
    print(''.join(o[int(a + b, 2)] for a, b in zip(s[i], s[i + h])))
