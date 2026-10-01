p = [complex(*map(int, input().split())) for i in range(int(input()))]
print('%.3f' % sum(abs(x - y) for x, y in zip([0] + p, p + [0])))
