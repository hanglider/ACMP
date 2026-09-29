n = int(input())
p = [(i // 10, i % 100) for i in range(100, 1000) if all(i % j for j in range(2, i))]
c = [0] * 100
for a, b in p:
    c[b] += 1
for _ in range(n - 3):
    e = [0] * 100
    for a, b in p:
        e[b] += c[a]
    c = [x % (10**9 + 9) for x in e]
print(sum(c) % (10**9 + 9))
