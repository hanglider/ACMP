def f(n, k):
    r = 0
    while n:
        n //= k
        r += n 
    return r

def F(n):
    s = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            s.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        s.append(n)
    return s

def m(t):
    a = {}
    for i in t:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1 
    return a

n = int(input())
t = F(n)
a = m(t)
y = 1e9
for i in a:
    y = min(y, f(n, i)//a.get(i))
print(y)