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

    for line in input_file:
        key_name, next_position = line.split(" = ")
        left, right = next_position.strip("(").strip(")").split(", ")
        positions[key_name] = [left, right]

    # print(positions["AAA"][0])

    # starts at AAA, loop through the directions and find the next position until ZZZ is reached
    current_position = "AAA"
    step = 0
    while current_position != "ZZZ":
        if directions[0] == "L": # go left if direction is L
            current_position = positions[current_position][0]
        else: # go right if direction is R
            current_position = positions[current_position][1]
        
        # remove the direction that was just taken, then add it to the end of the list
        directions.append(directions.pop(0))
        step += 1

    print("The number of steps to reach 'ZZZ' is : ", step)