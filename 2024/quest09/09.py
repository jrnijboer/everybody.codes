def build_steps(to):
    steps = [to] * (to + 1)
    steps[0] = 0
    for i in range(1, to + 1):
        for s in stamps:
            if i >= s:
                steps[i] = min(steps[i], steps[i - s] + 1)
    return steps

# part 1
brightness_list = [int(i) for i in open("09a.txt", encoding="utf-8").read().strip().split('\n')]
stamps = [1, 3, 5, 10]
steps = build_steps(max(brightness_list))
print("Answer part 1:", sum([steps[b] for b in brightness_list]))

# part 2
brightness_list = sorted([int(i) for i in open("09b.txt", encoding="utf-8").read().strip().split('\n')], reverse=True)
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
steps = build_steps(max(brightness_list))
print("Answer part 2:", sum([steps[b] for b in brightness_list]))

# part 3
brightness_list = sorted([int(i) for i in open("09c.txt", encoding="utf-8").read().strip().split('\n')], reverse=True)
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
steps = build_steps((max(brightness_list) - 100) // 2 + 100)
ans = 0
for brightness in brightness_list:
    start = brightness // 2 - 50
    end = start + 100
    pairs = [(a,(brightness - a)) for a in range(start, end + 1) if abs(a-(brightness - a)) <= 100]
    ans += min([steps[x] + steps[y] for x, y in pairs])
print("Answer part 3:", ans)
