n, k = input().split()
print(sorted(map(str, range(1, int(n) + 1))).index(k) + 1)
