a = ''.join(map(str.__add__, input().split(), input().split()))
d = {a: ''}
q = [a]
for x in q:
    if x == ''.join(c * 4 for c in x[::4]):
        print(d[x] or 'Solved')
        break
    for m, p in zip("F F' R R' U U'".split(), 'cadbeugvijklsntpqrhfomwx bdacetgsijklvnupqrmofhwx avcxefghtjrlompnqbsdukwi arctefghxjvlnpmoqksiubwd mncdabghefklijopsqtruvwx efcdijghmnklaboprtqsuvwx'.split()):
        y = ''.join(x[ord(c) - 97] for c in p)
        if y not in d:
            d[y] = d[x] + m
            q += [y]
