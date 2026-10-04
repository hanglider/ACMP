p = set()
for l in [*open(0)][2:]:
    o, *a = l.split()
    if o == "ADD":
        p.add(tuple(a))
    else:
        r = [i for i in range(1, 101) if ((str(i), a[0]) if o == "LISTSET" else (a[0], str(i))) in p]
        print(*r or [-1])
