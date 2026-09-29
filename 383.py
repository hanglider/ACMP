d = [sum(map(int, str(i))) for i in range(1000)]
print([i for i in range(1, 576397) if (d[i // 1000] + d[i % 1000]) % len(str(i)) < 1][int(input()) - 1])
