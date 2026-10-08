n, x, y = map(int, input().split())
a = [0]*(n+1)
a[n] = y 
a[n-1] = x
for i in range(n-2, -1, -1):
	a[i] = a[i+2] - a[i+1]
print(a[0], a[1])