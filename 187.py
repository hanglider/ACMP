n = int(input())
w = {}
for q in range(1 - n, n):
    for r in range(max(1 - n, 1 - n - q), min(n, n - q)):
        w[q, r] = w.get((q, r - 1), 0) + w.get((q - 1, r), 0) + w.get((q - 1, r + 1), 0) + ((q, r) == (1 - n, 0))
print(w[n - 1, 0])
