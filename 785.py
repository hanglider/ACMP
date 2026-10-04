a, b = map(int, input().split())
print(*[x for x in [1, 5, 6, 25, 76, 376, 625, 9376, 90625, 109376, 890625] if a <= x <= b])
