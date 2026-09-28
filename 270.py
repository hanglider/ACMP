import re
s = input()
if re.fullmatch('[a-z]+(_[a-z]+)*', s):
    print(re.sub('_(.)', lambda m: m[1].upper(), s))
elif re.fullmatch('[a-z][a-zA-Z]*', s):
    print(re.sub('([A-Z])', r'_\1', s).lower())
else:
    print('Error!')
