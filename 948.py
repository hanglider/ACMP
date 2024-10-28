K, N = map(int, input().split())
if N > K:
    if N % K != 0:
        print(N//K + 1, N % K)
    else:
        print(N//K, K)
elif N <= K:
    print(1, N)