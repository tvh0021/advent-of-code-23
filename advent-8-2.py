import numpy as np

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-8-0.txt"

if __name__ == "__main__":
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")

    # isolate the directions
    directions = list(input_file.pop(0))
    input_file.remove("")

    # print(directions)

    # create a dictionary to store the next position
    positions = dict()
    list_of_As = []
    list_of_Zs = []

    for line in input_file:
        key_name, next_position = line.split(" = ")
        left, right = next_position.strip("(").strip(")").split(", ")
        positions[key_name] = [left, right]

        # find all cases that starts with "xxA"
        if key_name[2] == "A":
            list_of_As.append(key_name)
        elif key_name[2] == "Z":
            list_of_Zs.append(key_name)

    # print(positions["AAA"][0])
    # print(list_of_As)
    # print(list_of_Zs)

    # starts at AAA, loop through the directions and find the next position until ZZZ is reached
    current_position = list_of_As.copy()
    step = 0
    mapper = dict()

    while step < 1e6:
        internal_counter = 0
        for j in range(len(current_position)):
            if directions[0] == "L": # go left if direction is L
                current_position[j] = positions[current_position[j]][0]
            else: # go right if direction is R
                current_position[j] = positions[current_position[j]][1]

            if current_position[j].endswith("Z"):
                internal_counter += 1
                mapper[list_of_As[j]] = [current_position[j], step+1]
                # print("Node ", list_of_As[j], " reached ", current_position[j], " at step ", step)

        # remove the direction that was just taken, then add it to the end of the list
        directions.append(directions.pop(0))
        step += 1

        # if all A nodes have reached Z at least once, then break
        if len(mapper) == len(list_of_As):
            print(step)
            break

    print("Mapper : ", mapper)

    step_to_reach_each_node = []
    for key in mapper.keys():
        step_to_reach_each_node.append(mapper[key][1])

    # the number of steps to reach all nodes at the same time is the least common multiple of all the steps to reach each node
    print("The number of steps to reach all nodes ending with 'Z' is : ", np.lcm.reduce(step_to_reach_each_node))