import re
import sys

lines = sys.stdin.read().split("\n")
n = int(lines[0].split()[0])
vocabulary = set(word.strip() for word in lines[1:n + 1])
text = "\n".join(lines[n + 1:]).lower()
used = set(re.findall(r"[a-z]+", text))

if not used <= vocabulary:
    print("Some words from the text are unknown.")
elif vocabulary - used:
    print("The usage of the vocabulary is not perfect.")
else:
    print("Everything is going to be OK.")
