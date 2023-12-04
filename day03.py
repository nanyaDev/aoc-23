from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    arr = [[ch for ch in line] for line in data]


def access(array, x, y):
    if 0 <= x < len(array) and 0 <= y < len(array[x]):
        return {"index": (x, y), "value": array[x][y]}
    else:
        return {"index": (x, y), "value": "."}


gears = defaultdict(list)
total = 0
for i, row in enumerate(arr):
    start = None
    for j, ch in enumerate(row):
        if not ch.isnumeric():
            continue

        if start is None:
            start = j

        if access(arr, i, j + 1)["value"].isnumeric():
            continue

        surroundings = [
            access(arr, i - 1, start - 1),
            access(arr, i, start - 1),
            access(arr, i + 1, start - 1),
            access(arr, i - 1, j + 1),
            access(arr, i, j + 1),
            access(arr, i + 1, j + 1)
        ]

        num = ''
        for _j in range(start, j + 1):
            num += arr[i][_j]
            surroundings.append(access(arr, i - 1, _j))
            surroundings.append(access(arr, i + 1, _j))

        if any(not ch["value"].isnumeric() and ch["value"] != '.' for ch in surroundings):
            total += int(num)

        for el in surroundings:
            if el["value"] == '*':
                gears[el["index"]].append(num)

        start = None

ratio = 0
for parts in gears.values():
    if len(parts) == 2:
        ratio += int(parts[0]) * int(parts[1])

print("Part 1: ", total)
print("Part 2: ", ratio)
