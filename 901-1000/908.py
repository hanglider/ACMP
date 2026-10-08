n = int(input())
a = []
a.append(0)
a.append(1)
a.append(1)
for i in range(3,n):
	t = i + 1
	if (t % 2 == 0) and (t % 3 == 0):
		a.append((min(a[i - 1],min(a[i//2],a[i//3]))) + 1)
	elif t % 2 == 0:
		a.append((min(a[i - 1],a[i//2])) + 1)
	elif t % 3 == 0:
		a.append((min(a[i - 1],a[i//3])) + 1)
	else:
		a.append(a[i-1]+1)
print(a[n-1])