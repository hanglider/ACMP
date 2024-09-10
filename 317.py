x, y, z, w = map(int, input().split())
ans = 0
for i in range((w // x)+1):
    for j in range((w // y)+1):
        k = w - i*x - j*y
        if  ((k) % z == 0) and (k>=0): ans += 1
print(ans)