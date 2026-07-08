import sys
D = sys.stdin.read().split()
k = int(D[0])
i = 1
O = []
for _ in range(k):
    a = int(D[i]); b = int(D[i+1]); c = int(D[i+2]); e = int(D[i+3])
    i += 4
    A, B = a, b
    r = "NO"
    while True:
        if A == c and B == e:
            r = "YES"
            break
        if B == 0:
            break
        if B > A:
            A, B = B, A
            if A == c and B == e:
                r = "YES"
                break
            if B == 0:
                break
        if e == B and 0 <= c <= A and (A - c) % B == 0:
            r = "YES"
            break
        A, B = A % B, B
    O.append(r)
print('\n'.join(O))
