n = int(input())
d = []
ans = ''
for _ in range(n):
	a = list(map(int, input().split()))
	if len(a) == 1:
		if a[0] == 3:
			ans += str(d[0]) + ' '
			d = d[1:]
		else:
			l = len(d)
			ans += str(d[l-1]) + ' '
			d = d[:(l-1)]
		#print(d)
	else:
		if a[0] == 1:
			d.insert(0,a[1])
		else:
			d.append(a[1])
	#print(d)
print(ans)