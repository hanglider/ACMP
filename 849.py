from itertools import *
n = int(input())
a = [range(2, n + 1, 2), range(1, n + 1, 2)]
if n % 6 == 2:
    a = [a[0], [3, 1], range(7, n + 1, 2), [5]]
if n % 6 == 3:
    a = [range(4, n + 1, 2), [2], range(5, n + 1, 2), [1, 3]]
g = map("%d %d".__mod__, zip(count(1), chain(*a)))
if n in (2, 3):
    print("No solution")
else:
    while s := list(islice(g, 9**5)):
        print("\n".join(s))
