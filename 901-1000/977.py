from math import comb

# graphs on n labelled vertices with no isolated vertex, by inclusion-exclusion
# over the set of vertices forced to be isolated
n = int(open("INPUT.TXT").read())
total = 0
for k in range(n + 1):
    rest = n - k
    total += (-1) ** k * comb(n, k) * 2 ** (rest * (rest - 1) // 2)
open("OUTPUT.TXT", "w").write(str(total) + "\n")
