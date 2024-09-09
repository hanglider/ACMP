n, m = map(int, input().split())
t = 0
while n > 0:
    t = t ^ 2
    n -= 1
while m > 0:
    t = t ^ 3
    m -= 1
if t == 0:
    print(2)
else:
    print(1)