data = open("INPUT.TXT").read().split()
t = int(data[0])
out = []
for i in range(t):
    k = int(data[1 + 2 * i])
    p = int(data[2 + 2 * i])
    if p < 70 and k >= (1 << p):
        out.append("No solution")
    else:
        out.append(str((k & -k).bit_length()))
open("OUTPUT.TXT", "w").write("\n".join(out) + "\n")
