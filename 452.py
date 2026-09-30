f = [1, 2]
for i in range(260):
    f.append(f[-1] + f[-2])
s = sum(f[len(x) - 1 - i] for x in open(0).read().split() for i in range(len(x)) if x[i] == '1')
r = ''
for x in f[::-1]:
    r += str(s // x)
    s %= x
print(r.lstrip('0'))
