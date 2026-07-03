def solve():
    with open('INPUT.TXT') as f:
        n = int(f.read())
    result = []
    def gen(current, stack):
        if len(current) == n:
            if not stack:
                result.append(current)
            return
        if len(stack) < n - len(current):
            gen(current + '(', stack + ['('])
            gen(current + '[', stack + ['['])
        if stack:
            closing = ')' if stack[-1] == '(' else ']'
            gen(current + closing, stack[:-1])
    gen('', [])
    with open('OUTPUT.TXT', 'w') as f:
        f.write('\n'.join(result))

solve()
