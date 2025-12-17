# part 1
instructions = { k.strip(): [v.strip() for v in vals.split(",")] for t in open("07a.txt", encoding="utf-8") if ":" in t for k, vals in [t.strip().split(":", 1)] }
powers = {k: 10 for k in instructions}


for k in instructions:
    score = 0
    power = 10
    for i in range(10):
        ix = i % len(instructions[k])
        delta = 1 if instructions[k][ix] == '+' else -1 if instructions[k][ix] == '-' else 0
        power += delta
        score = max(score + power, 0)
    powers[k] = score

# part 2
keys_sorted_by_value = sorted(powers, key=powers.get,reverse=True)
print("Answer part 1:", "".join(keys_sorted_by_value))

instructions = { k.strip(): [v.strip() for v in vals.split(",")] for t in open("07b.txt", encoding="utf-8") if ":" in t for k, vals in [t.strip().split(":", 1)] }
powers = {k: 10 for k in instructions}
track_input = [line.strip() for line in open("trackb.txt", encoding="utf-8").readlines()]
for line in track_input[1:-1]:
    track_input[0] = track_input[0] + line[-1]
    track_input[-1] = line[0] + track_input[-1]
track = track_input[0] + track_input[-1][::-1]
track = track[1:] + track[0]

for k in instructions:
    scores = []
    power = 10
    step = 0
    for j in range(10):
        for i, ch in enumerate(track):
            if ch == "=" or ch == "S":
                ix = step % len(instructions[k])
                delta = 1 if instructions[k][ix] == '+' else -1 if instructions[k][ix] == '-' else 0
            elif ch == "+":
                delta = 1
            elif ch == "-":
                delta = -1
            step += 1
            power += delta
            scores.append(power)
    powers[k] = sum(scores)

keys_sorted_by_value = sorted(powers, key=powers.get,reverse=True)
print("Answer part 2:", "".join(keys_sorted_by_value))

# part 3
from collections import Counter
import math

def generate_permutations(counter, path, results):
    if sum(counter.values()) == 0:
        results.append(''.join(path))
        return
    for char in list(counter):
        if counter[char] > 0:
            counter[char] -= 1
            generate_permutations(counter, path + [char], results)
            counter[char] += 1

def get_unique_permutations(s):
    counter = Counter(s)
    results = []
    generate_permutations(counter, [], results)
    return results

actions = get_unique_permutations("+++++---===")
track_input = [line.strip() for line in open("/home/jan/git/everybody.codes/2024/quest07/trackc.txt", encoding="utf-8").readlines()]
rival_string = open("07c.txt", encoding="utf-8").read().strip().split(":")[1].replace(',','')
track_string = "+"
visited = set((0, 1))
next = (0, 2)
while next != (0, 1):
    y, x = next
    visited.add(next)
    track_string += track_input[y][x]
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if 0 <= y + dy < len(track_input) and 0 <= x + dx < len(track_input[y+dy]) and track_input[y+dy][x+dx] != ' ' and (y+dy, x+dx) not in visited:
            next = (y+dy, x+dx)
            break

for i, action in enumerate(actions):
    scores = []
    power = 10
    step = 0
    if i % 500 == 0:
        print('.', end='', flush=True)
    for j in range(len(action) // math.gcd(len(track_string), len(action))):
        for i, ch in enumerate(track_string):
            if ch == "=" or ch == "S":
                ix = step % len(action)
                delta = 1 if action[ix] == '+' else -1 if action[ix] == '-' else 0
            elif ch == "+":
                delta = 1
            elif ch == "-":
                delta = -1
            step += 1
            power += delta
            scores.append(power)
    powers[action] = sum(scores)

print("\nAnswer part 3:", len([v for v in powers.values() if v > powers[rival_string]]))
