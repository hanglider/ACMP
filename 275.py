for s in open(0).read().split()[1:]:
    print(['No', 'Yes'][int(s, 2) % 7 < 1])
