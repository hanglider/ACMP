x, y = map(int, input().split())
p = [0] * (y+1)
a = 1
t = []
g = print
for i in range(2, y+1):
    if p[i] == 0:
        s = i+i 
        while s < len(p):
            p[s] = 1
            s += i 
        if i >= x:
            a = 0
            t += [str(i)]
g("\n".join(t))
if a:
    g("Absent")