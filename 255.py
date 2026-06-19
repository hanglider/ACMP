with open('input.txt', 'r') as f:
    n = int(f.read().strip())

d = n
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        d = i
        break

a = n // d
b = n - a

print(a, b)
