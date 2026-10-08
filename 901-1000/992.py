# Removing dominoes always leads to the same irreducible diagram: the 2-core.
# Compute it on the 2-runner abacus of beta-numbers.
k = int(input())
rows = list(map(int, input().split()))
betas = [rows[i] + (k - 1 - i) for i in range(k)]
even = sum(1 for b in betas if b % 2 == 0)
odd = k - even
positions = sorted([2 * i for i in range(even)] + [2 * i + 1 for i in range(odd)], reverse=True)
core = [positions[i] - (k - 1 - i) for i in range(k)]
core = [x for x in core if x > 0]
print(1)
print(len(core), *core)
