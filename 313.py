a = open(0).read().split()[1:]
d = {x: i for i, x in enumerate(set(a))}
b = bytes(map(d.get, a))
print(max(max(map(len, b.split(bytes([c]))[1:-1]), default=-1) for c in d.values()) + 1)
