p = sorted(tuple(map(int, input().split())) for _ in range(int(input())))
print(["No", "Yes"][len({tuple(map(sum, zip(a, b))) for a, b in zip(p, p[::-1])}) < 2])
