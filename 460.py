n = int(input())
k = 0
ans = 0
razr = 1
zz, b = 0, 0
komb = [0]*20
for i in range(20):
	komb[i] = i * pow(10,i - 1).__trunc__()
while n > 0:
	zz = n % 10
	n = n // 10
	if zz > 5:
		ans += zz * komb[k] + razr
	if zz == 5:
		ans += 5 * komb[k] + b + 1
	if zz < 5:
		ans += zz * komb[k]
	b = zz * razr + b 
	razr *= 10
	k += 1 
print(ans)