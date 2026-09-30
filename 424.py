n = int(input())
while n > 18:
    n = -(-n // 18)
print(["Stan", "Ollie"][n > 9], "wins.")
