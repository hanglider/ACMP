import sys


def main():
    n, x, y = map(int, sys.stdin.read().split())
    size = 1 << n
    board = [[0] * size for _ in range(size)]
    counter = [0]

    def tile(top, left, s, hr, hc):
        # fill square (top, left, s) where cell (hr, hc) is already occupied
        if s == 1:
            return
        h = s // 2
        counter[0] += 1
        num = counter[0]
        holes = []
        for dr in (0, 1):
            for dc in (0, 1):
                qt = top + dr * h
                ql = left + dc * h
                if qt <= hr < qt + h and ql <= hc < ql + h:
                    holes.append((qt, ql, hr, hc))
                else:
                    cr = qt + (h - 1 if dr == 0 else 0)
                    cc = ql + (h - 1 if dc == 0 else 0)
                    board[cr][cc] = num
                    holes.append((qt, ql, cr, cc))
        for qt, ql, r, c in holes:
            tile(qt, ql, h, r, c)

    tile(0, 0, size, y - 1, x - 1)
    print("\n".join(" ".join(map(str, row)) for row in board))


main()
