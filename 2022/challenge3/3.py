from input3 import *

# https://adventofcode.com/2022/day/3
# Time: 30 Mins

# Part One
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lookup = {j: i + 1 for i, j in enumerate(list(alpha))}
total = 0
for rucksack in a.splitlines():
    first = rucksack[: len(rucksack) // 2]
    second = rucksack[len(rucksack) // 2 :]
    total += alpha_lookup[next(i for i in first if i in second)]

# Part Two
total = 0
rucksacks = a.splitlines()
grouped_rucksacks = [
    rucksacks[i * 3 : (i * 3) + 3] for i in range(0, len(rucksacks) // 3)
]
for first, second, third in grouped_rucksacks:
    total += alpha_lookup[next(i for i in first if i in second and i in third)]
