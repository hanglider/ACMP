a, b = open("INPUT.TXT").read().split()
open("OUTPUT.TXT", "w").write(str(int(a, 3) + int(b, 3)))
