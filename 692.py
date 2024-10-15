def is_binary_number(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

n = int(input())
if is_binary_number(n):
    print(f"YES")
else:
    print(f"NO")
