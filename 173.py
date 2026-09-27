n = int(input())
r = []
for b in range(2, 37):
    d = []
    x = n
    while x:
        d += [x % b]
        x //= b
    if d == d[::-1]:
        r += [b]
print(["none", "unique", "multiple"][min(len(r), 2)])
if r:
    print(*r)
