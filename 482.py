n = int(input())
s = ""
for i in range(1, 179):
    t = ""
    for j in range(1, i):
        t += str(j)
    s += t
print(s[n-1])