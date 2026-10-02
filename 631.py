n = int(input())
a = b = 1
c = 0
while a < n:
    a, b = b, a + b
    c += 1
print(c)
