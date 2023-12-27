from collections import Counter

with open('input.txt', 'r') as f:
    lines = [line.split(' ') for line in f.read().splitlines()]


def get_value(hand):
    values = {
        'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
        '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
    }

    c = list(sorted(Counter(hand).values(), reverse=True))
    v = [values.get(x) for x in hand]

    return c, v


def get_value_with_joker(hand):
    values = {
        'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8,
        '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1,
    }

    _hand = [x for x in hand if x != 'J']

    c = list(sorted(Counter(_hand).values(), reverse=True))
    v = [values.get(x) for x in hand]

    # JJJJJ edge case
    if len(c) == 0:
        c = [5]

    c[0] += 5 - sum(c)

    return c, v


ranked_hands = sorted(lines, key=lambda x: get_value(x[0]))
total = 0
for i, h in enumerate(ranked_hands):
    total += int(h[1]) * (i + 1)

print("Part 1: ", total)

ranked_hands = sorted(lines, key=lambda x: get_value_with_joker(x[0]))
total = 0
for i, h in enumerate(ranked_hands):
    total += int(h[1]) * (i + 1)

print("Part 2: ", total)
