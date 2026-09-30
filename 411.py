a, b, c = map(int, input().split())
d = b * b - 4 * a * c
r = []
if a:
    if d >= 0:
        r = sorted({(-b - d**.5) / 2 / a, (-b + d**.5) / 2 / a})
elif b:
    r = [-c / b]
elif c == 0:
    exit(print(-1))
print(len(r))
for x in r:
    print(x + 0)
