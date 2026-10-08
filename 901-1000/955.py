data = open("INPUT.TXT").read().split()
n, m = int(data[0]), int(data[1])
k = int(data[2])
blocked = [[False] * m for _ in range(n)]
for i in range(k):
    y = int(data[3 + 2 * i]) - 1
    x = int(data[4 + 2 * i]) - 1
    blocked[y][x] = True

# count connected components of free cells
components = 0
for sy in range(n):
    for sx in range(m):
        if blocked[sy][sx]:
            continue
        components += 1
        blocked[sy][sx] = True
        stack = [(sy, sx)]
        while stack:
            y, x = stack.pop()
            for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                if 0 <= ny < n and 0 <= nx < m and not blocked[ny][nx]:
                    blocked[ny][nx] = True
                    stack.append((ny, nx))

open("OUTPUT.TXT", "w").write(str(components))
