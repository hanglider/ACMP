s = input()
n = len(s)
print(max(l for l in range(n) if len({(*sorted(s[i:i + l]),) for i in range(n - l + 1)}) < n - l + 1))
