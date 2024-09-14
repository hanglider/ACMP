def f(a, n, p):
    if n:
        for i in range(n+1, 0, -1):
            if i <= p:
                f(a+[i], n-i, i)
    else:
        print(*a, sep='+')
  
  
n = int(input())
f([], n, n-1)