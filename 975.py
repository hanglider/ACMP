def solve(N, K):
    sN = str(N)
    LN = len(sN)
    p10 = [1]
    for _ in range(20): p10.append(p10[-1]*10)

    prefN = [0]*(LN+1)
    for i in range(1, LN+1): prefN[i] = prefN[i-1]*10 + (ord(sN[i-1])-48)
    sufN = [0]*(LN+1)
    for i in range(LN-1, -1, -1): sufN[i] = (ord(sN[i])-48)*p10[LN-1-i] + sufN[i+1]

    def feasible(pref, Lp):
        for L in range(Lp, LN+1):
            t = L - Lp
            a = pref * p10[t]
            if L < LN:
                b = a + p10[t] - 1
            else:  # L == LN
                pn = prefN[Lp]
                if pref > pn: 
                    continue
                b = a + (p10[t]-1 if pref < pn else sufN[Lp])
            if a <= b and a + (-a) % K <= b:
                return True
        return False

    P = 0
    Lp = 0
    while True:
        if Lp and P % K == 0 and P <= N:
            return P
        digs = range(1, 10) if Lp == 0 else range(10)
        for d in digs:
            q = P*10 + d
            if feasible(q, Lp+1):
                P, Lp = q, Lp+1
                break

while True:
    try:
        N, K = map(int, input().split())
    except:
        break
    if N == 0 and K == 0:
        break
    print(solve(N, K))
