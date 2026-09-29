q, p = sorted(map(int, input().split()))
b, a = sorted(map(int, input().split()))
l = b * (p * p + q * q) - 2 * p * q * a
print("Possible" if p <= a and q <= b or p > a > q < b and l >= 0 and l * l >= (p * p - q * q)**2 * (p * p + q * q - a * a) else "Impossible")
