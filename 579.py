n = int(input())
a = list(map(int, input().split()))
ps = 0
os = 0
p = []
o = []
for i in range(n):
	if a[i] > 0:
		ps += a[i]
		p.append(i+1) 
	else:
		os += a[i]
		o.append(i+1)
if abs(os) < ps:
	print(len(p))
	print(*p)
else:
	print(len(o))
	print(*o)
