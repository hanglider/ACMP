d, m = map(int, input().split())
x = (d - m) % 3 < 1
if d > 27 and m in (1, 3):
    x = d * m in (30, 93)
print(1 + x)
