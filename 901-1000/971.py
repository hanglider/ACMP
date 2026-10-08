x, y = map(int, open("INPUT.TXT").read().split())
limit = 10 ** 9
with open("OUTPUT.TXT", "w") as out:
    if abs(x) == limit or abs(y) == limit:
        # all vertices would share this coordinate, so the triangle degenerates
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(f"{x + 1} {y}\n{x} {y + 1}\n{x - 1} {y - 1}\n")
