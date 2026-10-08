data = list(map(int, open("INPUT.TXT").read().split()))
n = data[0]
coins = data[1:n + 1]
k = data[n + 1]
sums = data[n + 2:n + 2 + k]

limit = max(sums)
can = [False] * (limit + 1)
can[0] = True
for s in range(1, limit + 1):
    for c in coins:
        if c <= s and can[s - c]:
            can[s] = True
            break

open("OUTPUT.TXT", "w").write(" ".join("1" if can[s] else "0" for s in sums))
