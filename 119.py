n = int(input())
d = {}
for i in range(n):
    c, m, s = map(int, input().split())
    d[(c,m,s,i)] = c*3600 + m*60 + s 
a = sorted(d.items(), key=lambda x: x[1])
for i in a:
    print(i[0][0],i[0][1],i[0][2])