s = input()
d = [[]]
for i in range(len(s)):
    d.append(min((d[j] + [s[j:i + 1]] for j in range(i + 1) if s[j:i + 1] == s[j:i + 1][::-1]), key=len))
print(len(d[-1]), *d[-1], sep="\n")
