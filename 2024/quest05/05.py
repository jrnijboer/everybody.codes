from collections import defaultdict

def dance(D, round):
    c = D[round][0]
    D[round] = D[round][1:]
    nxt = (round + 1) % 4
    pos = (c - 1) % (2 * len(D[nxt]))

    if pos < len(D[nxt]):
        D[nxt] = D[nxt][:pos] + [c] + D[nxt][pos:]
    else:
        pos = 2 * len(D[nxt]) - pos
        D[nxt] = D[nxt][:pos] + [c] + D[nxt][pos:]


lst = [[int(x) for x in line.split()] for line in open("05a.txt")]
D = dict(enumerate(map(list, zip(*lst))))
for i in range(10):
    dance(D, i % 4)
print("Part 1 answer:", int(''.join(str(D[j][0]) for j in range(4))))

lst = [[int(x) for x in line.split()] for line in open("05b.txt")]
D = dict(enumerate(map(list, zip(*lst))))
shouts = defaultdict(int)
i = 0
while True:
    dance(D, i % 4)
    shout = int(''.join(str(D[j][0]) for j in range(4)))
    shouts[shout] += 1
    if shouts[shout] == 2024:
        print("Part 2 answer:", (i + 1) * shout)
        break
    i += 1

lst = [[int(x) for x in line.split()] for line in open("05c.txt")]
D = dict(enumerate(map(list, zip(*lst))))
i, best = 0, 0
states = set()
while True:
    state = tuple(x for k in range(4) for x in D[k])
    if state in states:
        print("Part 3 answer:", best)
        break
    dance(D, i % 4)
    states.add(state)
    shout = int(''.join(str(D[j][0]) for j in range(4)))
    shout = max(shout, best)
    i += 1
