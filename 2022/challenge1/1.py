from input1 import a

# https://adventofcode.com/2022/day/1
# Time: 7:35.26

b = a.split("\n\n")  # Split input by groups
c = [i.split("\n") for i in b]  # Split individual groups out
d = [[int(j) for j in i] for i in c]  # Convert all numbers to int
e = [sum(i) for i in d].sort()  # Sum the groups
print(e[-1])  # Print the top one
print(e[-1] + e[-2] + e[-3])  # Print the top three
