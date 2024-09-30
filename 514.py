def solve():
	n = int(input())
	kub = 1
	while n > 0:
		n -= kub
		kub += 1
	if n < 0 :
		print(kub-2)
	else:
		print(kub-1)
	return 0

t = 1
#t = int(input())
while t > 0:
	solve()
	t -= 1