from itertools import *
from operator import *
input()
s = sorted(accumulate(map({"a": 1, "b": -1}.get, input())))
z = s.count(0)
s = bytes(map(eq, s, islice(s, 1, None)))
l = list(map(len, s.split(b"\0")))
print((sum(map(mul, l, l)) + s.count(1)) // 2 + z)
