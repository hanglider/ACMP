n, v, k = map(int, input().split())
print('YNEOS'[v <= (n - 1) * k::2], sum(max(0, v - i * k) for i in range(n)))
