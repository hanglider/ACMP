n, *a = map(int, open(0).read().split())
s = sum(a)
t = s // 3
b = [1]
for x in a:
    b += [b[-1] | b[-1] << x]
if s % 3 or b[n] >> t & 1 < 1:
    print(0)
else:
    r = []
    for i in range(n, 0, -1):
        if b[i - 1] >> t & 1 < 1:
            t -= a[i - 1]
            r += [i]
    print(len(r))
    print(*r[::-1])
