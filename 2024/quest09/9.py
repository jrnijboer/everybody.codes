from math import inf

beetles = [[1, 3, 5, 10], \
        [1, 3, 5, 10, 15, 16, 20, 24, 25, 30], \
        [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]]

def get_input(part):

    with open(f'09b.txt', 'r') as f:
        s = f.read()
    return s


def solve(part):
    inp = [int(i) for i in open("09b.txt", encoding="utf-8").read().strip().split('\n')]
    mx = max(inp)

    mn = [0]
    while mx >= (len(mn) if part < 3 else ((len(mn)/2) + 200)):
        mn.append(inf)
        for b in beetles[part-1]:
            if b >= len(mn):
                break
            mn[~0] = min(mn[~b]+1, mn[~0])

    if part < 3:
        return sum(mn[i] for i in inp)

    ans = 0
    for n in inp:
        l = (n - 99) // 2
        r = n - l
        ians = inf
        while l <= r:
            ians = min(mn[l] + mn[r], ians)
            l += 1
            r -= 1
        ans += ians
    return ans

print(solve(2))
