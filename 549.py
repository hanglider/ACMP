p, q = map(int, input().split())
i = 1
a = []
while p:
    i += 1
    p *= i
    a += [p // q]
    p %= q
print(i, *a, sep="\n")
