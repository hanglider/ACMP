import fractions
op = fractions.Fraction(1, 1000)
def solve():
    n = int(input())
    d = {}
    for i in range(n):
        s1, s2 = map(str, input().split())
        a = int(s1)
        k = 1
        if len(s2) > 1:
            if s2[0] == "m":
                k = op
            elif s2[0] == "k":
                k = 1000
            elif s2[0] == "M":
                k = 1000000
            elif s2[0] == "G":
                k = 1000000000
        l = len(s2)
        t = 1
        if s2[l-1] == 'p':
            t = a*k*16380
        elif s2[l-1] == 'g':
            t = a*k
        elif s2[l-1] == 't':
            t = a*k*1000000
        d[(i, t)] = (a, s2)
    ans = sorted(d.items(), key=lambda x: x[0][1])
    print()
    for i in range(n):
        print(ans[i][1][0], ans[i][1][1])
    pass
 
t = 1
#t = int(input())
while t > 0:
    solve()
    t -= 1