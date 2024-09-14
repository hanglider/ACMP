import math
def fib(i):
    x = 0
    y = 1
    k = 2
    while k != i:
        buf = y
        y += x 
        x = buf
        k += 1
        x = x % const
        y = y % const
    return y
i, j = map(int, input().split())
const = 1e9.__trunc__()
#print(math.gcd(i,j))
print(fib(math.gcd(i,j)+1) % const)