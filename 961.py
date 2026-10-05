import sys


def main():
    data = sys.stdin.read().split()
    n, m = int(data[0]), int(data[1])
    first = data[2:2 + n]
    second = data[2 + n:2 + 2 * n]

    def positions(grid):
        pos = {}
        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                if ch != '.':
                    pos[ch] = (i, j)
        return pos

    before = positions(first)
    after = positions(second)
    moving = [ch for ch in before if before[ch] != after.get(ch)]
    moving.sort(key=lambda ch: (ch.isupper(), ch))
    print(len(moving))
    print("".join(moving))


main()
