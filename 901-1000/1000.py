import sys

numbers = sys.stdin.read().split()
n = int(numbers[0])
out = []
for token in numbers[1:n + 1]:
    x = int(token)
    for q in range(8):
        bits = 7 * (q + 1)  # value bits after q ones and a zero
        if -(1 << (bits - 1)) <= x < (1 << (bits - 1)):
            total = 8 * (q + 1)
            code = (((1 << q) - 1) << (total - q)) | (x & ((1 << bits) - 1))
            out.append(format(code, "0%dx" % (2 * (q + 1))))
            break
    else:
        out.append("ff" + format(x & ((1 << 64) - 1), "016x"))
print("\n".join(out))
