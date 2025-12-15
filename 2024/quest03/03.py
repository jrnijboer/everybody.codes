def solve(filename, depth, diagonals):
    grid = [line.strip() for line in open(filename, encoding="utf-8").readlines()]
    G = {(x, y): 0 if c == "." else 1 for y, line in enumerate(grid) for x, c in enumerate(line)}

    def dig(depth):
        newGrid, digs = dict(), 0
        for (x,y), d in G.items():
            if d == depth and G[(x-1, y)] == depth and G[(x+1,y)] == depth and G[x, y-1] == depth and G[x, y+1] == depth \
                    and (not diagonals or (G[(x-1, y-1)] == depth and G[(x+1,y+1)] == depth and G[x+1, y-1] == depth and G[x-1, y+1] == depth )):
                newGrid[(x,y)] = depth + 1
                digs += 1
            else:
                newGrid[(x,y)] = G[(x,y)]
        return newGrid, digs

    while True:
        G, changed = dig(depth)
        depth += 1
        if changed == 0:
            break

    return sum(G.values())

print("Part 1:", solve("03a.txt", 1, False))
print("Part 2:", solve("03b.txt", 1, False))
print("Part 3:", solve("03c.txt", 1, True))
