n = int(input())
print([i for i in range(10**5) if len(set(str(i))) == len(str(i))][n])
