n, m = map(int, input().split())
ans = 2 % m
for i in range(n):
	ans = ans*ans % m
print(ans)