s = input()
m = len(s) + 2
p = q = [0] * m
f = [1] + p[1:]
for c in s[::-1]:
    if c == '(':
        p = f
    else:
        q = f
    f = [(b == 0) + p[b + 1] + q[b - 1] for b in range(m - 1)] + [0]
print(f[0])
