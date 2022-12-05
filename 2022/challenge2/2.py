from input2 import *

# https://adventofcode.com/2022/day/2
# Time; 50 mins because I didn't want to use all if/else

# A for Rock, B for Paper, and C for Scissors.
# response: X for Rock, Y for Paper, and Z for Scissors.
# 1 for Rock, 2 for Paper, and 3 for Scissors
# outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
b = a.replace("X", "1")
b = b.replace("Y", "2")
b = b.replace("Z", "3")
b = b.replace("A", "1")
b = b.replace("B", "2")
b = b.replace("C", "3")
c = [[int(j) for j in i.split(" ")] for i in b.splitlines()]
score_total = 0
for elf_response, my_response in c:
    if elf_response == my_response:
        score_total += 3 + my_response  # Draw
    elif (
        (elf_response == 1 and my_response == 2)
        or (elf_response == 2 and my_response == 3)
        or (elf_response == 3 and my_response == 1)
    ):
        score_total += 6 + my_response  # Win
    elif (
        (elf_response == 1 and my_response == 3)
        or (elf_response == 2 and my_response == 1)
        or (elf_response == 3 and my_response == 2)
    ):
        score_total += my_response  # Loss
print(score_total)


b = a.replace("X", "0")
b = b.replace("Y", "3")
b = b.replace("Z", "6")
b = b.replace("A", "1")
b = b.replace("B", "2")
b = b.replace("C", "3")
c = [[int(j) for j in i.split(" ")] for i in b.splitlines()]
loss_table = [0, 3, 1, 2]
win_table = [0, 2, 3, 1]

score_total = 0
for elf_response, result in c:
    if result == 3:
        score_total += result + elf_response
    elif result == 0:  # loss
        score_total += result + loss_table[elf_response]
        # 1 = 3
        # 2 = 1
        # 3 = 2
    elif result == 6:
        score_total += result + win_table[elf_response]
        # 1 = 2
        # 2 = 3
        # 3 = 1
