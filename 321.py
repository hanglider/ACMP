n = int(input())
r = []
for b in range(2, 37):
    d = []
    m = n
    while m:
        d += [m % b]
        m //= b
    if len(d) == len(set(d)):
        r += [b]
print(*r)
