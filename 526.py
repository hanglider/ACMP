a, b = open(0).read().split()
print(next((x for x in range(max(2, int(max(a), 36) + 1), 37) if int(a, x) == int(b)), 0))
