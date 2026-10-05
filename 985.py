import re

lines = open("INPUT.TXT").read().split("\n")
n = int(lines[0])
sizes = {}
for i in range(1, n + 1):
    name, size = lines[i].split()
    sizes[name] = int(size)
m = int(lines[n + 1])
out = []
for i in range(n + 2, n + 2 + m):
    line = lines[i].strip()
    type_name = re.match(r"\s*([a-z]+)", line).group(1)
    dims = [int(x) for x in re.findall(r"\[\s*(\d+)\s*\]", line)]
    total = sizes[type_name]
    for d in reversed(dims):
        total = 24 + d * total
    out.append(str(total))
open("OUTPUT.TXT", "w").write("\n".join(out) + "\n")
