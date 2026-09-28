b = bin(int(input()))[2:]
print(max(int(b[i:] + b[:i], 2) for i in range(len(b))))
