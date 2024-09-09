x1, y1, x2, y2 = map(int, input().split(' '))
xA, yA = map(int, input().split(' '))
if y1 == y2:
    print(xA, y1 + (y1 - yA))
if x1 == x2:
    print(x1 + (x1 - xA), yA)