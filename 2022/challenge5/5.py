from input5 import *

# https://adventofcode.com/2022/day/5
# Time: 54:39

split_arrangement_vertically = [[i[(j*4)+1] for j in range(0,9)] for i in array.splitlines()]
split_arrangement_horizontally = [[split_arrangement_vertically[j][i] for j in range(0,8) if split_arrangement_vertically[j][i] != ' '] for i in range(0, 9)]
sanitised_movements = movements.replace("move ", " ").replace(" from ", " ").replace(" to ", " ")
movement_array = [[int(j) for j in i.split()] for i in sanitised_movements.splitlines()]


for count, from_stack, to_stack in movement_array:
    from_stack -= 1
    to_stack -= 1

    for _ in range(0, count):
        from_container = split_arrangement_horizontally[from_stack].pop(0)
        print(f"took {from_container} from {from_stack} to {to_stack}")
        split_arrangement_horizontally[to_stack] = [from_container] + split_arrangement_horizontally[to_stack]

part_1_arrangement = [i for i in split_arrangement_horizontally] # Deep copy
part_1_answer = ''.join([i.pop(0) for i in part_1_arrangement])
print(f"answer a is: {part_1_answer}")


split_arrangement_horizontally = [[split_arrangement_vertically[j][i] for j in range(0,8) if split_arrangement_vertically[j][i] != ' '] for i in range(0, 9)]
for count, from_stack, to_stack in movement_array:
    from_stack -= 1
    to_stack -= 1

    from_container = [split_arrangement_horizontally[from_stack].pop(0) for _ in range(0, count)]
    print(f"took {from_container} from {from_stack} to {to_stack}")
    split_arrangement_horizontally[to_stack] = from_container + split_arrangement_horizontally[to_stack]

part_2_arrangement = [i for i in split_arrangement_horizontally] # Deep copy
part_2_answer = ''.join([i.pop(0) for i in part_2_arrangement])
print(f"answer 2 is: {part_2_answer}")