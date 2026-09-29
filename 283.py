import re
print("YNeos"[not re.fullmatch("([A-Z][a-z]{1,3})+", input())::2])
