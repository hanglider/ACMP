t = []
k = 0
try:
    for c in input():
        if c in '([':
            t += c
        else:
            k += t.pop() + c in '(][)'
    print(-1 if t else k)
except:
    print(-1)
