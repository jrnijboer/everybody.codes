from collections import Counter
creatures = Counter(list(open("01a.txt", encoding="utf-8").read()))
defense = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}
res = creatures["B"] + 3*creatures["C"]
print("Part 1:", res)

creatures = list(open("01b.txt", encoding="utf-8").read())
res = 0
for i in range(0, len(creatures)-1, 2):
    first, second = creatures[i], creatures[i+1]
    if first != "x" and second != "x":
        res += 2
    res += defense[first] + defense[second]
print("Part 2:", res)

creatures = list(open("01c.txt", encoding="utf-8").read())
res = 0
for i in range(0, len(creatures)-2, 3):
    first, second, third = creatures[i], creatures[i+1], creatures[i+2]
    cntr = Counter([first, second, third])
    if cntr["x"] == 1:
        res += 2
    if cntr["x"] == 0:
        res += 6
    res += defense[first] + defense[second] + defense[third]
print("Part 3:", res)