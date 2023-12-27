import re
from math import lcm

with open('input.txt', 'r') as f:
    lines = [line for line in f.read().splitlines()]

lr = [ch for ch in lines[0]]

nodes = {}
for line in lines[2:]:
    n, l, r = re.findall(r'\w+', line)
    nodes[n] = (l, r)


def trace_node1(node):
    i = 0
    j = 0
    while True:
        i += 1

        dir_i = 0 if lr[j] == 'L' else 1

        node = nodes[node][dir_i]

        if node == 'ZZZ':
            break

        j = j + 1 if j + 1 < len(lr) else 0

    return i


def trace_node2(node):
    i = 0
    j = 0
    while True:
        i += 1

        dir_i = 0 if lr[j] == 'L' else 1

        node = nodes[node][dir_i]

        if node[-1] == 'Z':
            break

        j = j + 1 if j + 1 < len(lr) else 0

    return i


print("Part 1: ", trace_node1('AAA'))
print("Part 2: ", lcm(*[trace_node2(n) for n in nodes.keys() if n[-1] == 'A']))
