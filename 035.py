k = int(input())
for _ in range(k):
    n, m = map(int, input().split())
    print(19*m + (n + 239)*(n + 366) // 2)