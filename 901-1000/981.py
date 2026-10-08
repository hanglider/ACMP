from itertools import product as P
s = input().strip()
e = s.replace('!', ' not ').replace('&', ' and ').replace('|', ' or ')
R = lambda g, S: next((v for v in S if all(g(a) == a[v] for a in (dict(zip(S, p)) for p in P((0, 1), repeat=len(S))))), 0) or '<' + R(lambda a: g({**a, S[1]: a[S[0]]}), S[:1] + S[2:]) + R(lambda a: g({**a, S[2]: a[S[1]]}), S[:2] + S[3:]) + R(lambda a: g({**a, S[0]: a[S[2]]}), S[1:]) + '>'
print(R(lambda a: eval(e, {}, a), sorted({*filter(str.isalpha, s)})))