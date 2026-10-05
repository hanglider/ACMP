import sys

data = sys.stdin.buffer.read().split()
n, k = int(data[0]), int(data[1])
scores = set(map(int, data[2:2 + n]))
queries = map(int, data[2 + n:2 + n + k])
print(' '.join('YES' if q in scores else 'NO' for q in queries))
