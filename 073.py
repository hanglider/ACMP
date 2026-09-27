print("".join(chr((int(c, 27) - i) % 27 + 96) for i, c in enumerate(input(), 1)).replace("`", " "))
