import sys

board = [list(line.strip()) for line in sys.stdin.read().split()[:8]]


def captures(me, enemy):
    taken = set()

    def dfs(r, c):
        for dr in (-1, 1):
            for dc in (-1, 1):
                mr, mc = r + dr, c + dc
                tr, tc = r + 2 * dr, c + 2 * dc
                if 0 <= tr < 8 and 0 <= tc < 8 and board[mr][mc] == enemy and board[tr][tc] == '.':
                    taken.add((mr + 1, mc + 1))
                    board[mr][mc] = '.'
                    board[r][c] = '.'
                    board[tr][tc] = me
                    dfs(tr, tc)
                    board[tr][tc] = '.'
                    board[r][c] = me
                    board[mr][mc] = enemy

    for r in range(8):
        for c in range(8):
            if board[r][c] == me:
                dfs(r, c)
    return sorted(taken)


for name, me, enemy in (("White", 'W', 'B'), ("Black", 'B', 'W')):
    cells = captures(me, enemy)
    print(f"{name}: {len(cells)}")
    if cells:
        print(", ".join(f"({r}, {c})" for r, c in cells))
