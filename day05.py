import re

with open('input.txt', 'r') as f:
    lines = [line for line in f.read().splitlines()]

_seeds, *blocks = '\n'.join(lines).split('\n\n')
seeds = [int(x) for x in re.findall(r'(\d+)', _seeds)]


def calculate_location(seed):
    curr = seed
    for block in blocks:
        for nums in block.splitlines()[1:]:
            dest, src, rg = [int(x) for x in re.findall(r'(\d+)', nums)]

            if src <= curr <= src + rg - 1:
                curr = dest + (curr - src)
                break

    return curr


locations = [calculate_location(seed) for seed in seeds]
print("Part 1: ", min(locations))

locations = {}
for i in range(0, len(seeds), 2):
    start = seeds[i]
    end = seeds[i] + seeds[i + 1]

    seed = start
    while seed < end:
        location = calculate_location(seed)
        locations[seed] = location

        skips = 1
        while True:
            _skips = skips * 2
            _seed = seed + _skips

            if _seed >= end:
                break

            if calculate_location(_seed) == location + _skips:
                skips = _skips
            else:
                break

        seed += skips

print("Part 2: ", min(locations.values()))
