def isp(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

n = int(open("input.txt").read())
while True:
    if isp(n):
        print(n)
        break
    if n < 10:
        print(0)
        break
    n = sum(int(c) for c in str(n))
