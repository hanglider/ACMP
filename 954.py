k = int(open("INPUT.TXT").read())
MOD = 10 ** 6

# ways[h] = number of sequences of groups (heights 10, 11, 12) with total height h
ways = [0] * (k + 1)
ways[0] = 1
for h in range(10, k + 1):
    ways[h] = (ways[h - 10] + ways[h - 11] + (ways[h - 12] if h >= 12 else 0)) % MOD

# the first glass can be placed bottom down or bottom up
open("OUTPUT.TXT", "w").write(str(2 * ways[k] % MOD))
