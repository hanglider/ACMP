n, m, *a = map(int, open(0).read().split())
e = {*zip(a[::2], a[1::2])}
k = 1
while k:
    k = {x for x, y in e} - {y for x, y in e}
    e = {(x, y) for x, y in e if x not in k}
print(["No", "Yes"][not e])
