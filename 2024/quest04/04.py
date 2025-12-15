nails = sorted([int(s.strip()) for s in  open("04a.txt", encoding="utf-8").readlines()])
goal = nails[0]
print("Part 1 answer:", sum([n - goal for n in nails[1:]]))

nails = sorted([int(s.strip()) for s in  open("04b.txt", encoding="utf-8").readlines()])
goal = nails[0]
print("Part 2 answer:", sum([n - goal for n in nails[1:]]))

nails = sorted([int(s.strip()) for s in  open("04c.txt", encoding="utf-8").readlines()])
goal = (nails[len(nails) // 2 - 1] + nails[len(nails) // 2 ]) // 2
print("Part 3 answer:", sum([abs(n - goal) for n in nails]))
