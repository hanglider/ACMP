f = input
a = f()
b = f()
c = ""
while a*len(b)>"":
	if a + b < b + a:
		c += a[0]
		a = a[1:]
	else:
		c += b[0]
		b = b[1:]
print(c+a+b)