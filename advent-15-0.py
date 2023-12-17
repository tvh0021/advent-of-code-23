file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-15-0.txt"

def convertToHASH(ascii_code : list[int]) -> int:
    current_value = 0
    for code in ascii_code:
        current_value = (current_value + code) * 17 % 256
    
    return current_value

if __name__ == "__main__":
    with open(file_path, "r") as f:
        input_file = f.read().split(",")
    
    # part 1
    # convert each string to its ascii code, then calculate the associated hash
    hash_per_line = []
    for string in input_file:
        hash_per_line.append(convertToHASH([ord(i) for i in string]))
    
    print("Part 1")
    print("Sum of all hashes : ", sum(hash_per_line))

        
    # calculate the focal length and string of each line
    focal_lengths = [0] * len(input_file)
    actual_strings = [''] * len(input_file)
    hash_per_line = []  
    for i, string in enumerate(input_file):
        if "=" in string:
            actual_strings[i], focal_lengths[i] = string.split("=")
        else:
            actual_strings[i] = string.split("-")[0]
            focal_lengths[i] = str(-1)
        hash_per_line.append(convertToHASH([ord(j) for j in actual_strings[i]]))

    # print("Strings : ", actual_strings)
    # print("Focal lengths : ", focal_lengths)
    # print("Label : ", hash_per_line)
    
    # for each line, check if the instruction to to remove or insert/replace the lens. If it is to remove, remove the lens from the box. If it is to insert/replace, check if the lens is already in the box. If it is, replace with the new lens label. If it is not, insert the lens.

    # create a dictionary that contains boxes from 0 to 255
    boxes = dict()
    for i in range(256):
        boxes[i] = list()

    for i in range(len(input_file)):
        # print("Line : ", i)
        # print("Box : ", boxes[hash_per_line[i]])

        if focal_lengths[i] == str(-1):
            try:
                for j in range(len(boxes[hash_per_line[i]])):
                    if actual_strings[i] == boxes[hash_per_line[i]][j].split(" ")[0]:
                        boxes[hash_per_line[i]].pop(j)
                        break
            except ValueError:
                pass
        else:
            string_in_box = False
            for j in range(len(boxes[hash_per_line[i]])):
                if actual_strings[i] == boxes[hash_per_line[i]][j].split(" ")[0]:
                    boxes[hash_per_line[i]][j] = actual_strings[i] + " " + focal_lengths[i]
                    string_in_box = True
                    break
            if not string_in_box:
                boxes[hash_per_line[i]].append(actual_strings[i] + " " + focal_lengths[i])

        # print the boxes
        # print("New box : ", boxes[hash_per_line[i]])
    
    # print the non-empty boxes
    for i in range(256):
        if len(boxes[i]) > 0:
            print("Box ", i, " : ", boxes[i])

    # sum up the focusing power
    focusing_power = 0
    for i in range(256):
        if len(boxes[i]) == 0:
            continue

        for j in range(len(boxes[i])):
            focusing_power += (i + 1) * (j + 1) * int(boxes[i][j].split(" ")[1])

    print("Part 2")
    print("Focusing power : ", focusing_power)
            
        
    
    
    
    
    
    