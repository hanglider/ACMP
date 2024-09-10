n = int(input())
ans = 0
for i in range(n):
    if int(str(i)[::-1]) + i == n:
        ans += 1
print(ans)