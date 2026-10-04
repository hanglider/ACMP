n = int(input())
print(n - 2**(n.bit_length() - 1))
