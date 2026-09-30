s = [c for c in input() if 'a' <= c.lower() <= 'z']
t = [c.lower() for c in s]
n = len(t)
i = 0
while i < n - 1 - i and t[i] == t[n - 1 - i]:
    i += 1
j = n - 1 - i
f = lambda a: a == a[::-1]
if f(t[i + 1:j]):
    s[i] = s[j]
elif f(t[i + 1:j + 1]):
    del s[i]
elif f(t[i:j]):
    del s[j]
else:
    s = 0
print(s and 'YES\n' + ''.join(s) or 'NO')
