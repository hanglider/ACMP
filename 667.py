N, M, K = map(int, input().split())
if N == 0:
    r = 0 if M == 0 else -(-M // K)
elif K < 3:
    r = 0
else:
    x = -(-N // (K - 2))
    if M < 2 * x:
        r = 0
    else:
        e = M - 2 * x
        l = x * K - (N + 2 * x)
        rem = max(0, e - l)
        r = x + -(-rem // K)
print(r)
