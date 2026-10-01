R, r, h, b = map(int, input().split())
print(["NO", "YES"][max(h + r - b, b - r)**2 + r * r <= R * R])
