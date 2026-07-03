data = open('input.txt').read().split()
ptr = 0
n = int(data[ptr]); ptr += 1
S = list(map(int, data[ptr:ptr + n])); ptr += n
k = int(data[ptr]); ptr += 1
V = list(map(int, data[ptr:ptr + k])); ptr += k

order = sorted(range(n), key=lambda i: -S[i])
mach = sorted(range(k), key=lambda j: -V[j])[:min(n, k)]
m = len(mach)

T = sum(S) / sum(V[j] for j in mach)
pp = vv = 0
for idx in range(m - 1):
    pp += S[order[idx]]
    vv += V[mach[idx]]
    T = max(T, pp / vv)

EPS = 1e-7
machines = [[V[j] * T, [(0.0, T, float(V[j]), j)]] for j in mach]
res = []

for i in order:
    p = float(S[i])
    machines.sort(key=lambda x: -x[0])
    hit = -1
    for idx in range(len(machines)):
        if abs(machines[idx][0] - p) < EPS:
            hit = idx
            break
    if hit < 0 and p >= machines[0][0]:
        hit = 0
    if hit >= 0:
        for s, e, spd, ph in machines[hit][1]:
            if e - s > 1e-12:
                res.append((s, i, ph))
        del machines[hit]
        continue
    a = 0
    while a + 1 < len(machines) and machines[a + 1][0] > p:
        a += 1
    A = machines[a][1]
    B = machines[a + 1][1] if a + 1 < len(machines) else []
    fa = lambda t: sum(spd * max(0.0, min(e, t) - s) for s, e, spd, ph in A)
    fb = lambda t: sum(spd * max(0.0, e - max(s, t)) for s, e, spd, ph in B)
    bps = sorted({x for s, e, spd, ph in A + B for x in (s, e)})
    prev_t = bps[0]
    prev_f = fa(prev_t) + fb(prev_t)
    tau = bps[-1]
    for t2 in bps[1:]:
        f2 = fa(t2) + fb(t2)
        if f2 >= p:
            tau = prev_t if f2 - prev_f < 1e-12 else prev_t + (p - prev_f) * (t2 - prev_t) / (f2 - prev_f)
            break
        prev_t, prev_f = t2, f2
    for s, e, spd, ph in A:
        if min(e, tau) - s > 1e-12:
            res.append((s, i, ph))
    for s, e, spd, ph in B:
        if e - max(s, tau) > 1e-12:
            res.append((max(s, tau), i, ph))
    comp = [(s, min(e, tau), spd, ph) for s, e, spd, ph in B if min(e, tau) - s > 1e-12]
    comp += [(max(s, tau), e, spd, ph) for s, e, spd, ph in A if e - max(s, tau) > 1e-12]
    cap = sum((e - s) * spd for s, e, spd, ph in comp)
    if a + 1 < len(machines):
        del machines[a + 1]
    del machines[a]
    machines.append([cap, comp])

res.sort()
out = [f"{T:.7f}"]
for t, i, ph in res:
    out.append(f"{t:.7f} {i + 1} {ph + 1}")
print('\n'.join(out))
