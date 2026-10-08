n, *w = open(0).read().split()
d = {}
for x in w:
    d.setdefault(''.join(sorted(x)), []).append(x)
for g in sorted(d.values(), key=lambda g: (-len(g), min(g)))[:5]:
    print(f'Group of size {len(g)}:', *sorted(set(g)), '.')
