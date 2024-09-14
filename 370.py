n = int(input())
x, y = map(int, input().split())
xa, ya = x, y
S = 0
for _ in range(n - 1):
    xb, yb = map(int, input().split())
    S += xa * yb - ya * xb
    xa, ya = xb, yb
S += xa * y - ya * x
area = abs(S) / 2
print(f"{area:.1f}")