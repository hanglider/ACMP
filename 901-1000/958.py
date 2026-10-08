import sys


def main():
    lines = sys.stdin.read().split("\n")
    n, k = map(int, lines[0].split())
    rows = [lines[1 + i].strip() for i in range(n)]
    # goes(a, b): road goes from a to b (1-based)
    def goes(a, b):
        return rows[a - 1][b - 1] == '-'

    routes = []
    for line in lines[1 + n:]:
        nums = list(map(int, line.split()))
        if nums:
            routes.append(nums[1:-1])
        if len(routes) == k:
            break

    merged = []
    for route in routes:
        result = []
        i = j = 0
        while i < len(merged) and j < len(route):
            if goes(merged[i], route[j]):
                result.append(merged[i])
                i += 1
            else:
                result.append(route[j])
                j += 1
        result.extend(merged[i:])
        result.extend(route[j:])
        merged = result

    print(" ".join(map(str, [1] + merged + [n])))


main()
