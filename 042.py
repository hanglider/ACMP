n = int(input())
if n == 0:
    print(0)
    raise SystemExit
if n == 1:
    print(1)
    raise SystemExit
if n == 2:
    print(2)
    raise SystemExit
if n % 3 == 0:
    print(pow(3,n//3))
else:
    off = 0
    while n % 3 !=0:
        n -= 2
    off += 1
    print(pow(2,off)*pow(3,n // 3))