NOTES = {"A": 0, "A#": 1, "Bb": 1, "B": 2, "C": 3, "C#": 4, "Db": 4, "D": 5,
         "D#": 6, "Eb": 6, "E": 7, "F": 8, "F#": 9, "Gb": 9, "G": 10, "G#": 11, "Ab": 11}

tokens = open("INPUT.TXT").read().split()
n = int(tokens[0])
strings = [NOTES[s] for s in tokens[1:7]]
chord = tokens[7]

if chord.endswith("m7"):
    root_name, intervals = chord[:-2], [0, 3, 7, 10]
elif chord.endswith("7"):
    root_name, intervals = chord[:-1], [0, 4, 7, 10]
elif chord.endswith("m"):
    root_name, intervals = chord[:-1], [0, 3, 7]
else:
    root_name, intervals = chord, [0, 4, 7]
root = NOTES[root_name]
index_of = {(root + d) % 12: i for i, d in enumerate(intervals)}
full = (1 << len(intervals)) - 1

# dp[mask] = number of ways for processed strings giving exactly this set of chord notes
dp = {0: 1}
for open_note in strings:
    new_dp = {}
    for fret in range(n + 1):
        note = (open_note + fret) % 12
        if note not in index_of:
            continue
        bit = 1 << index_of[note]
        for mask, cnt in dp.items():
            new_dp[mask | bit] = new_dp.get(mask | bit, 0) + cnt
    dp = new_dp

open("OUTPUT.TXT", "w").write(str(dp.get(full, 0)))
