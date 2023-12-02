import re

with open('input.txt', 'r') as f:
    data = f.read().splitlines()
    lines = [line for line in data]

game_id_sum = 0
for line in lines:
    game_id, data = line.split(':')

    game_id = re.findall(r'(\d+)', game_id)[0]
    grabs = re.findall(r'(\d+) (\w+)', data)

    possible = True
    for n, color in grabs:
        if color == 'red' and int(n) > 12:
            possible = False
            break
        if color == 'green' and int(n) > 13:
            possible = False
            break
        if color == 'blue' and int(n) > 14:
            possible = False
            break

    if possible:
        game_id_sum += int(game_id)

print("Part 1: ", game_id_sum)

power_sum = 0
for line in lines:
    _, data = line.split(':')

    grabs = re.findall(r'(\d+) (\w+)', data)

    red_max = 0
    green_max = 0
    blue_max = 0
    for n, color in grabs:
        if color == 'red' and int(n) > red_max:
            red_max = int(n)
        if color == 'green' and int(n) > green_max:
            green_max = int(n)
        if color == 'blue' and int(n) > blue_max:
            blue_max = int(n)

    power_sum += red_max * green_max * blue_max

print("Part 2: ", power_sum)
