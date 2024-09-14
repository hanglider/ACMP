def binpow(a, n): 
    res = 1
    while n:
        if n & 1:
            res *= a
        a *= a
        n >>= 1
    return res
 
a, n = map(int, input().split())
print(binpow(a, n))