d = [1] + [0] * 81
for c in input():
    d = [(c != ")") * x + (c != "(") * y for x, y in zip([0] + d, d[1:] + [0])]
print(d[0])
