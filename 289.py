def e(n):
    s = list(range(n + 1))
    s[1] = 0
    for i in s:
        if i > 1:
            for j in range(i + i, len(s), i):
                s[j] = 0
    return [x for x in s if x != 0]
 
p = e(5000)
 
def G(a):
    c = 1
    for i in range(len(a)):
        c *= p[i]**(a[i] - 1)
    return c
 
def F(n):
    def b(r, c, s=2):
        if r == 1:
            f.append(list(c))
            return
        for i in range(s, n + 1):
            if r % i == 0:
                c.append(i)
                b(r // i, c, i)
                c.pop()
 
    f = []
    b(n, [])
    return f
 
n = int(input())
a = F(n)
q = 1e16
for x in a:
    q = min(q, G(sorted(x)[::-1]))
print(0 if q > 1e15 + 1 else q)