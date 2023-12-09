import numpy as np

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-9-0.txt"

def get_next_in_sequence(sequence, reverse=False):
    step = 1

    if reverse:
        sequence = np.flip(sequence)
    last_element_of_sequence = [sequence[-1]]

    while np.unique(sequence).size != 1:
        sequence = np.diff(sequence)
        print("Remaining sequence : ", sequence)
        print("Last digit : ", sequence[-1])
        last_element_of_sequence.append(sequence[-1])
        step += 1
    
    print("The number of steps is : ", step)

    return last_element_of_sequence

if __name__ == "__main__":
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")

    next_instance_array = np.empty(len(input_file),dtype=int)
    for l, line in enumerate(input_file):
        sequence = np.array([int(i) for i in line.strip().split()])
        print("Sequence : ", sequence)
        next_instance_array[l] = np.sum(get_next_in_sequence(sequence, reverse=True))
    
    print("The sum of all next instances is : ", np.sum(next_instance_array))