s = input()
n = len(s)
print(sum(len({s[i:i + l] for i in range(n - l + 1)}) for l in range(1, n + 1)))
