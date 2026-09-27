from ipaddress import *
s = open(0).read().split()
n = int(s[0])
f = lambda i: int(ip_address(s[i]))
k = [bin(f(i)).count("1") for i in range(1, n + 1)]
r = [sum(x <= j for x in k) for j in range(33)]
for i in range(n + 2, len(s), 2):
    print(r[32 - (f(i) ^ f(i + 1)).bit_length()])
