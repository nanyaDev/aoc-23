import re

with open('input.txt', 'r') as f:
    lines = [line for line in f.read().splitlines()]

times = [int(n) for n in re.findall(r'(\d+)', lines[0])]
distances = [int(n) for n in re.findall(r'(\d+)', lines[1])]

product = 1
for i in range(0, len(times)):
    t = times[i]
    d = distances[i]

    count = 0
    for j in range(0, t):
        if j * (t - j) > d:
            count += 1

    product *= count

print("Part 1: ", product)

time = int(''.join(re.findall(r'(\d+)', lines[0])))
distance = int(''.join(re.findall(r'(\d+)', lines[1])))

count = 0
for j in range(0, time):
    if j * (time - j) > distance:
        count += 1

print("Part 2: ", count)



