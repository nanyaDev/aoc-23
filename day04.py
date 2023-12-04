import re

with open('input.txt', 'r') as f:
    lines = [line for line in f.read().splitlines()]

total = 0
for line in lines:
    _, nums = line.split(':')
    w, n = nums.split('|')

    ww = re.findall(r'(\d+)', w)
    nn = re.findall(r'(\d+)', n)

    score = 0
    for nnn in nn:
        if nnn in ww:
            score = score + 1 if score == 0 else score * 2

    total += score

print("Part 1: ", total)

scores = [0] * len(lines)
for i, line in enumerate(lines):
    _, nums = line.split(':')
    w, n = nums.split('|')

    ww = re.findall(r'(\d+)', w)
    nn = re.findall(r'(\d+)', n)

    for nnn in nn:
        if nnn in ww:
            scores[i] = scores[i] + 1

copies = [1] * len(lines)
for i, score in enumerate(scores):
    for ii in range(i+1, i+1+score):
        copies[ii] += copies[i]

print("Part 2: ", sum(copies))
