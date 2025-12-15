from collections import defaultdict
T = { k.strip(): [v.strip() for v in vals.split(",")] for t in open("06a.txt", encoding="utf-8") if ":" in t for k, vals in [t.strip().split(":", 1)] }
Q = [('RR', '')]
strengths = defaultdict(list)

while Q:
    node, path = Q.pop()
    if node == '@':
        strengths[len(path)].append(path+'@')
    else:
        for nxt in T[node]:
            if nxt in T or nxt == '@':
                Q.append((nxt, path+node))

for k, v in strengths.items():
    if len(v) == 1:
        print("Answer part 1:", v[0])

T = { k.strip(): [v.strip() for v in vals.split(",")] for t in open("06b.txt", encoding="utf-8") if ":" in t for k, vals in [t.strip().split(":", 1)] }
Q = [('RR', '')]
strengths = defaultdict(list)

while Q:
    node, path = Q.pop()
    if node == '@':
        strengths[len(path)].append(path+'@')
    else:
        for nxt in T[node]:
            if nxt in T or nxt == '@':
                Q.append((nxt, path + ',' + node))

for k, v in strengths.items():
    if len(v) == 1:
        print("Answer part 2:",  "".join(s[0] for s in v[0][1:].split(",")) + "@")

T = { k.strip(): [v.strip() for v in vals.split(",")] for t in open("06c.txt", encoding="utf-8") if ":" in t for k, vals in [t.strip().split(":", 1)] }
Q = [('RR', '')]
strengths = defaultdict(list)

seen = {}
while Q:
    node, path = Q.pop(0)
    if node in seen and node != '@':
        path = seen[node]
        strengths[len(path)].append(path+'@')
        continue

    if node == '@':
        strengths[len(path)].append(path+'@')
    else:
        for nxt in T[node]:
            if nxt in T or nxt == '@':
                Q.append((nxt, path + ',' + node))
                seen[node] = path + ',' + node

for k, v in strengths.items():
    if len(v) == 1:
        print("Answer part 3:",  "".join(s[0] for s in v[0][1:].split(",")) + "@")
