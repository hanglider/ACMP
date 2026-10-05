def score(times):
    elapsed = 0
    solved = 0
    penalty = 0
    for t in times:
        elapsed += t
        if elapsed > 300:
            break
        solved += 1
        penalty += elapsed
    return (-solved, penalty)


data = open("INPUT.TXT").read().split()
n = int(data[0])
times = list(map(int, data[1:n + 1]))
students = [(score(sorted(times)), 1), (score(times[::-1]), 3), (score(times), 5)]
open("OUTPUT.TXT", "w").write(str(min(students)[1]))
