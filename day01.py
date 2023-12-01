import regex as re

with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    lines = [line for line in data]

total = 0
for line in lines:
    x = 0
    y = 0

    for ch in line:
        if ch.isnumeric():
            x = ch
            break

    for ch in line[::-1]:
        if ch.isnumeric():
            y = ch
            break

    total += int(x + y)

print("Part 1: ", total)

total = 0
for line in lines:
    x = 0
    y = 0

    matches = re.findall(r'(\d{1}|one|two|three|four|five|six|seven|eight|nine)', line, overlapped=True)

    x = matches[0]
    y = matches[-1]

    if x == 'one':
        x = '1'
    if x == 'two':
        x = '2'
    if x == 'three':
        x = '3'
    if x == 'four':
        x = '4'
    if x == 'five':
        x = '5'
    if x == 'six':
        x = '6'
    if x == 'seven':
        x = '7'
    if x == 'eight':
        x = '8'
    if x == 'nine':
        x = '9'

    if y == 'one':
        y = '1'
    if y == 'two':
        y = '2'
    if y == 'three':
        y = '3'
    if y == 'four':
        y = '4'
    if y == 'five':
        y = '5'
    if y == 'six':
        y = '6'
    if y == 'seven':
        y = '7'
    if y == 'eight':
        y = '8'
    if y == 'nine':
        y = '9'

    total += int(x + y)
    
print("Part 2: ", total)

