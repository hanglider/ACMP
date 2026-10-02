s = input()
print(max(int(s[:i] + s[i + 1:j] + s[j + 1:]) for j in range(len(s)) for i in range(j)))
