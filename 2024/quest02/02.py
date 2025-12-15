runics, words = open("02a.txt", encoding="utf-8").read().strip().split("\n\n")
runics = runics.split(":")[1].split(",")

print("Part 1:", sum([words.count(runic) for runic in runics]))

runics, words = open("02b.txt", encoding="utf-8").read().strip().split("\n\n")
runics = runics.split(":")[1].split(",")
i = 0
runic_indexes = set()
while i < len(words):
    for runic in runics:
        if words[i:].startswith(runic) or words[i:].startswith(runic[::-1]):
            for j in range(len(runic)):
                runic_indexes.add(i + j)
    i += 1
print("Part 2:", len(runic_indexes))

runics, words = open("02c.txt", encoding="utf-8").read().strip().split("\n\n")
runics = runics.split(":")[1].split(",")
grid = [list(line) for line in words.strip().split("\n")]

runic_positions = set()
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        for rune in runics:
            if c == rune[0]:
                for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xx, yy = x, y
                    positions = set()
                    for i, ch in enumerate(rune):
                        if grid[yy][xx] == ch:
                            positions.add((xx, yy))
                        xx = (xx + dx) % len(grid[0])
                        yy = yy + dy
                        if yy >= len(grid) or yy < 0:
                            break
                    if (len(positions)) == len(rune):
                        runic_positions |= positions
print("Part 3:", len(runic_positions))
