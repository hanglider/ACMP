k = int(input())
print(*min((k // h - h + k - k // h * h, h, k // h) for h in range(1, int(k**0.5) + 1))[1:])
