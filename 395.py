from math import prod
l, r = map(int, input().split())
print(sum(x % prod(map(int, str(x))) < 1 for x in range(l, r + 1) if '0' not in str(x)))
