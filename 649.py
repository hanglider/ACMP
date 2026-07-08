N, K = map(int, input().split())
S = input()
c = [0] * 36
def f(x):
    return ord(x) - 97 if x.isalpha() else 26 + int(x)
l = 0
t = 0
for r in range(N):
    x = f(S[r])
    c[x] += 1
    while c[x] > K:
        c[f(S[l])] -= 1
        l += 1
    t += r - l + 1
print(t)
