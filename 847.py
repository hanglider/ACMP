a, b = input().split()
print(["NO", "YES"][sorted(a) == sorted(b) and all(map(str.__ne__, a, b))])
