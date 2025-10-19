def prefix_function(s: str):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

def main():
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    m = int(input().strip())
    patterns = [input().strip() for _ in range(m)]

    need = set(patterns)
    cnt = {p: 0 for p in need}

    for t in words:
        pi = prefix_function(t)
        k = len(t)
        while k > 0:
            s = t[:k]
            if s in cnt:
                cnt[s] += 1
            k = pi[k - 1]

    print(*[cnt.get(p, 0) for p in patterns], sep="\n")

if __name__ == "__main__":
    main()

