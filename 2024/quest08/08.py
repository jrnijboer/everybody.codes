# part 1
bricks = int(open("08a.txt", encoding="utf-8").read().strip()) - 1
width, iteration = 1, 1

while bricks > 0:
    iteration += 1
    width += 2
    bricks -= 2 * iteration - 1
print("Answer part 1:", width * bricks * -1)

# part 2
priests = int(open("08b.txt", encoding="utf-8").read().strip())
bricks = 20240000 - 1
acolytes = 1111
thickness = 1

width, iteration = 1, 2
while bricks > 0:
    thickness = (thickness * priests) % acolytes
    bricks -= (width + 2) * thickness
    width += 2
    iteration += 1
print("Answer part 2:", width * bricks * -1)

# part 3
priests = int(open("08c.txt", encoding="utf-8").read().strip())
bricks = [1]
acolytes = 10
thickness = 1
width = 1
while True:
    thickness = (thickness * priests) % acolytes + acolytes
    bricks = [brick + thickness for brick in bricks] + [thickness]
    required = 2 * thickness
    required += 2 * sum([b - (priests * (2 * len(bricks) - 1) * b) % acolytes for b in bricks[1:-1]])
    required += bricks[0] - (priests * (2 * len(bricks) - 1) * bricks[0]) % acolytes
    if required > 202400000:
        print("Answer part 3:", (202400000 - required) * -1)
        break
