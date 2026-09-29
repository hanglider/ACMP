import re
print(sum(x[0] != 39 for x in re.findall(rb"'[^'\n]*'?|//.*|\{[^}]*|\(\*[\s\S]*?(?:\*\)|$)", open(0, 'rb').read())))
