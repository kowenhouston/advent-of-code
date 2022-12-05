from input4 import *

# https://adventofcode.com/2022/day/4
# Time: 25:56 min

# Every section has a unique ID number, and each Elf is assigned a range of section IDs.

pairs = [[j for j in i.split(",")] for i in a.splitlines()]
part_one_count = 0
part_two_count = 0
for pair1, pair2 in pairs:
    lower1, upper1 = [int(i) for i in pair1.split("-")]
    lower2, upper2 = [int(i) for i in pair2.split("-")]
    if ((lower1 <= lower2) and (upper1 >= upper2)) or (
        (lower1 >= lower2) and (upper1 <= upper2)
    ):
        part_one_count += 1  # Full overlap of numbers
    elif ((upper1 >= lower2) and (lower1 <= upper2)) or (
        (upper2 >= lower1) and (lower2 <= upper1)
    ):
        part_two_count += 1  # Partial Overlap of numbers

print(part_one_count)
print(part_one_count + part_two_count)
