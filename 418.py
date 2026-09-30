a = []
b = []
x = m = 0
for c in input():
    if c == '<':
        if x:
            x -= 1
        elif a:
            x = a.pop()
    elif c == '^':
        if a:
            b += x,
            x = a.pop()
    elif c == '|':
        if b:
            a += x,
            x = b.pop()
    elif c == '\\':
        a += x,
        x = 0
    else:
        x += 1
        m = max(m, x)
print(m)
