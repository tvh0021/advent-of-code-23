import numpy as np
from functools import cache

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-12-0.txt"

@cache
def try_recursive(line : str, consecutive_broken : tuple, number_in_sequence : int) -> int:

    # if the line is empty but there are still consecutive broken, return 0
    # if the line is empty and there are no more consecutive broken, return 1
    if len(line) == 0:
        if (len(consecutive_broken) == 0) and (number_in_sequence == 0):
            return 1
        else:
            return 0
    
    total = 0
    
    # if the spring is either operational or unsure
    if "." == line[0] or "?" == line[0]:
        # if the first consecutive broken zero, move to the second consecutive broken
        if number_in_sequence > 0:
            if (consecutive_broken != ()) and (consecutive_broken[0] == number_in_sequence):
                total += try_recursive(line[1:], consecutive_broken[1:], 0)
        else:
            total += try_recursive(line[1:], consecutive_broken, 0)

    # if the spring is either broken or unsure, decrement the first consecutive broken by one
    if "#" == line[0] or "?" == line[0]:
        total += try_recursive(line[1:], consecutive_broken, number_in_sequence + 1)
    
    return total

        
if __name__ == "__main__":
    # read in the map
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")

    # list of lists, each list is a line of the map
    symbol_map = []
    broken_sequences = []
    for l, line in enumerate(input_file):
        before_space, after_space = line.split(" ")
        symbol_map.append(before_space)
        broken_sequences.append([int(i) for i in after_space.split(",")])
        
    sum_of_all_arrangements = 0
    for l in range(len(symbol_map)):
        line = symbol_map[l]
        this_sequence = tuple(broken_sequences[l])
        number_of_arrangements = try_recursive(line+".", this_sequence, 0)
        sum_of_all_arrangements += number_of_arrangements
        # print("Line : ", line)
        # print("Broken sequence : ", this_sequence)
        # print("Number of configurations : ", number_of_arrangements)
    print("---------------------------------------------------")
    print("Part 1")
    print("The total number of arrangements is : ", sum_of_all_arrangements)

    # for part 2, we first transform the data by multiplying the string by 5, adding a "?" in between
    sum_of_all_arrangements = 0
    for l in range(len(symbol_map)):
        line = symbol_map[l]
        this_sequence = tuple(broken_sequences[l]*5)
        number_of_arrangements = try_recursive(((line + "?") * 5)[:-1]+".", this_sequence, 0)
        sum_of_all_arrangements += number_of_arrangements
    print("---------------------------------------------------")
    print("Part 2")
    print("The total number of arrangements is : ", sum_of_all_arrangements)