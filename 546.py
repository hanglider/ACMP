n = int(input())
t = -n // 4 * -4
f = lambda x: x * (x <= n)
for i in range(1, t // 4 + 1):
    print(i, 1, f(t - 2 * i + 2), 2 * i - 1)
    print(i, 2, f(2 * i), f(t - 2 * i + 1))
