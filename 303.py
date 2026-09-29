s = input()
print(max(sum(map(int, t[::2])) - sum(map(int, t[1::2])) for i in range(len(s)) for t in [s[:i] + s[i + 1:]]))
