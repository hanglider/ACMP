n = int(input())
print(min(range(1, 2 * n), key=lambda x: (len(set(str(x))) > 2, abs(x - n))))
