import sys

CAP = 21      # p <= 20, so lengths above 20 are all the same to us
STABLE = 400  # capped lengths stop changing after at most 10 * 20 steps


def main():
    lines = sys.stdin.read().split()
    n, k, p = int(lines[0]), int(lines[1]), int(lines[2])
    w = lines[3]
    image = [[ord(ch) - 65 for ch in lines[4 + i]] for i in range(n)]

    # lengths[j][c] = min(CAP, len(f^j(c)))
    lengths = [[1] * n]
    for j in range(min(k, STABLE)):
        prev = lengths[-1]
        lengths.append([min(CAP, sum(prev[d] for d in image[c])) for c in range(n)])

    def length_at(j):
        return lengths[min(j, len(lengths) - 1)]

    def pick(word, q, lens):
        # find the letter of word covering position q (1-based) and the position inside it
        for c in word:
            if q <= lens[c]:
                return c, q
            q -= lens[c]
        return None

    found = pick([ord(ch) - 65 for ch in w], p, length_at(k))
    if found is None:
        print("-")
        return
    c, q = found
    r = k

    # steps from level r to r - 1 with r - 1 >= STABLE use the same lengths: skip cycles
    stable_steps = max(0, r - STABLE)
    if stable_steps:
        lens = length_at(STABLE)
        seen = {}
        step = 0
        while step < stable_steps:
            state = (c, q)
            if state in seen:
                cycle = step - seen[state]
                step += (stable_steps - step) // cycle * cycle
                seen = {}
                if step >= stable_steps:
                    break
            seen[state] = step
            c, q = pick(image[c], q, lens)
            step += 1
        r -= stable_steps

    while r > 0:
        c, q = pick(image[c], q, length_at(r - 1))
        r -= 1

    print(chr(65 + c))


main()
