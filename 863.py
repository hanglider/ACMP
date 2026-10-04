print(*sorted(range(int(input())), key=lambda x: bin(x + 2**16)[::-1]))
