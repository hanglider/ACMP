a, b, c = map(int, input().split())
t = set(str(a))
t &= set(str(b))
t &= set(str(c))
print(len(t))
a = sorted(list(t))
for i in a:
    print(i, end=' ')