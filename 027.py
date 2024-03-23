def main():
    a, b = map(int, input().split())
    n = int(input())
    matrix = [[0] * a for _ in range(b)]

    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        for j in range(y1, y2):
            for i in range(x1, x2):
                matrix[j][i] = 1

    sum = a * b
    for row in matrix:
        for val in row:
            sum -= val

    print(sum)

main()