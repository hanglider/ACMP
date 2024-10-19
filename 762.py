n = int(input())
ans = 0
while n > 1:
	ans += 1
	n += 2
	n //= 3 

print(ans)