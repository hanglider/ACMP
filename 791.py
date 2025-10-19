n = int(input())
r, c = divmod(n-1,8)
print(*sorted([n - 8] * (r > 0) + [n + 8] * (r < 7) + [n - 1] * (c > 0) + [n + 1] * (c < 7)))
