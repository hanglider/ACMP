import sys

lines = sys.stdin.read().split("\n")
p, n, k = map(int, lines[0].split())
names = [line.strip() for line in lines[1:p + 1]]
ids = " ".join(lines[p + 1:]).split()
taken = {}
result = []
for name, team_id in zip(names, ids):
    if len(result) == n:
        break
    if taken.get(name, 0) < k:
        taken[name] = taken.get(name, 0) + 1
        result.append(name + " #" + team_id)
print("\n".join(result))
