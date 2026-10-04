s = "".join(open(0).read().split())
b = int(s.translate({98: 49, 119: 48}), 2)
x = [0]
for i in range(16):
    e = 0
    for j in range(16):
        if abs(i // 4 - j // 4) + abs(i % 4 - j % 4) < 2:
            e |= 1 << j
    x += [v ^ e for v in x]
r = [bin(i).count("1") for i in range(65536) if x[i] ^ b in (0, 65535)]
print(min(r) if r else "Impossible")
