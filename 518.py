n, k = map(int, input().split())
w = n + 1
s = ''.join(input() + '1' for _ in range(n)) + '1' * w
l = len(s)
d = [1] + [0] * (l - 1)
for _ in range(k):
    d = [(s[i] < '1') * (d[i - 1] + d[i - w] + d[i + 1 - l] + d[i + w - l]) for i in range(l)]
print(d[n * w - 2])
