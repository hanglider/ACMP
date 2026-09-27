n = int(input())
a = [0, 2, 3, 4, 7, 13]
s = set(a)
b = [0]
x = 0
while len(b) <= n:
    x += 1
    if x not in s:
        b.append(x)
        if len(b) == len(a):
            a.append(b[-1] + b[-3])
            s.add(a[-1])
print(a[n], b[n], sep='\n')