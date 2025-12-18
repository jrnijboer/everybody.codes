# part 1
brightness_list = [int(i) for i in open("09a.txt", encoding="utf-8").read().strip().split('\n')]
stamps = [1, 3, 5, 10]
ans = 0
for b in brightness_list:
    div, b = divmod(b, max(stamps))
    Q = [(0,[])]
    while Q:
        cur, beetles = Q.pop(0)
        if cur == b:
            ans += len(beetles) + div
            break
        if cur > b:
            continue
        for s in stamps:
            Q.append((cur+s, beetles[:] + [s]))
print("Answer part 1:", ans)

# part 2
brightness_list = sorted([int(i) for i in open("09b.txt", encoding="utf-8").read().strip().split('\n')], reverse=True)
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]

steps = [max(brightness_list)] * (max(brightness_list) + 1)
steps[0] = 0
for i in range(1, max(brightness_list) + 1):
    for s in stamps:
        if i >= s:
            steps[i] = min(steps[i], steps[i - s] + 1)
print("Answer part 2:", sum([steps[b] for b in brightness_list]))

# part 3
brightness_list = sorted([int(i) for i in open("09c.txt", encoding="utf-8").read().strip().split('\n')], reverse=True)
stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
end = (max(brightness_list) - 100) // 2 + 100
steps = [end] * (end + 1)
steps[0] = 0
for i in range(1, end + 1):
    for s in stamps:
        if i >= s:
            steps[i] = min(steps[i], steps[i - s] + 1)
ans = 0
for brightness in brightness_list:
    start = brightness // 2 - 50
    end = start + 100
    pairs = [(a,(brightness - a)) for a in range(start, end + 1) if abs(a-(brightness - a)) <= 100]
    ans += min([steps[x] + steps[y] for x, y in pairs])
print("Answer part 3:", ans)
