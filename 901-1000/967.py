def digit_sum(x, base):
    total = 0
    while x:
        total += x % base
        x //= base
    return total


data = open("INPUT.TXT").read().split()
n, k1, k2 = int(data[0]), int(data[1]), int(data[2])
numbers = map(int, data[3:3 + n])
b = sorted(digit_sum(a, k1) * digit_sum(a, k2) for a in numbers)
open("OUTPUT.TXT", "w").write(" ".join(map(str, b)) + "\n")
