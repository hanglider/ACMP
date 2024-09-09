def f(x):
    if x == 1:
        return 1
    else:
        return x*f(x-1)
 
n, k = map(int, input().split())
if (n == 0) | (k == 0) | (k > n):
    print(0)
    raise SystemExit
if n == k:
    r = f(n)
else:
    r = 1
    for i in range(k):
        r = r*((n-i)*(n-i))
    r = r // f(k)
print(r)