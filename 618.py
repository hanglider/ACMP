from itertools import accumulate
x = int("6shq0e9dvfjgbzmkw5rcchwwdp2uwxmgqgphcx06ittinjhs9naf2ep3xiktx0qmtrmxgkrw15xu9micq7tpd384hgd4oaatf1uvx9yzv688qlcnnns8v1x9kxdfxhygdj2o7rjkcfcmphlj8jbg6ri5e10bcq6wkj1rywtz69bapo2bk1rilph7ro776acznrtlcakgncakym6mntppzenrh6jcj2m0ifqjzejnalv7xhl6w9j6zcxq6f9iqw5gvpebttky00kpld6260ltdyvoxwnbz50sz1y1tuxwfyam68utz92nbivdr5k0nhgq7cvfzvbjwegtzeqavw1d2w6ny5jw98tujmlis9v0tcwp93mdezjwpnwuk3jo7hbf0ux7ahjuoqp2vdjaoc3xjjxjr1k0uu9sr6oukb3h5qu8vpffosvjv4reuft4knus05k9ajpuu3bkc4kl07pbfkg99e7v3j9", 36)
n = int(input())
for i in range(n):
    w = 0
    r = []
    while sum(r) <= i:
        if x & 1:
            w += 1
        else:
            r = [w] + r
        x >>= 1
c = [1] * (r[0] + 1)
for m in r[1:]:
    c = list(accumulate(c[::-1]))[::-1][:m + 1]
print(sum(c) - 1)
print(*r)
