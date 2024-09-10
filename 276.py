N, M = map(int, input().split(' '))
tmp = N - N//M * M
for i in range(int(M - tmp)):
    print(str(N//M) + ' ')
for j in range(int(tmp)):
    print(str(N // M + 1) + ' ')