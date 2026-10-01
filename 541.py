s, t = open(0).read().split()
print(int(max(s[i:] + s[:i] for i in range(len(s)) if s[i] > '0')) - int(min(t[i:] + t[:i] for i in range(len(t)) if t[i] > '0')))
