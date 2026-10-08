lines = open("INPUT.TXT").read().split()
a, b = lines[0], lines[1]
n = len(a)
count_a = [a.count(chr(97 + c)) for c in range(26)]
count_b = [b.count(chr(97 + c)) for c in range(26)]
# Every pair of positions (i, j) is aligned in exactly n of the n*n shift pairs.
total = 0
for x in range(26):
    for y in range(26):
        diff = abs(x - y)
        total += count_a[x] * count_b[y] * min(diff, 26 - diff)
open("OUTPUT.TXT", "w").write(str(total * n) + "\n")
