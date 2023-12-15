import numpy as np
import matplotlib.pyplot as plt

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-14-0.txt"

def pushNorth(col : np.ndarray) -> np.ndarray:
    cube_rocks_pos = np.where(col == "#")[0]
    segments = np.split(col,cube_rocks_pos)
    # print("Segments : ", segments)
    
    for segment in segments:
        if len(segment) == 0:
            continue

        number_of_round_rocks = np.count_nonzero(segment == "O")
        if segment[0] == "#":
            segment[1:number_of_round_rocks+1] = "O" 
            segment[number_of_round_rocks+1:] = "."
        else:
            segment[:number_of_round_rocks] = "O" 
            segment[number_of_round_rocks:] = "."

    col = np.concatenate(segments)
    # print("New column : ", col)

    return col

def calculateLoad(modified_char_map : np.ndarray) -> int:
    number_of_rows = modified_char_map.shape[0]
    weight = np.arange(number_of_rows,0,-1)
    
    rowwise_sum = np.sum(modified_char_map == "O", axis=1)
    load = np.sum(rowwise_sum * weight)

    return load
    

if __name__ == "__main__":
    # read in the map
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")

    # convert map to numpy array
    char_map = np.chararray((len(input_file),len(input_file[0])),unicode=True)
    for l, line in enumerate(input_file):
        char_map[l] = np.array([i for i in line.strip("\n")])

    part1_map = char_map.copy()
    for k in range(part1_map.shape[1]):
        part1_map[:,k] = pushNorth(part1_map[:,k])


    # calculate the load
    load1 = calculateLoad(part1_map)
    print("Part 1")
    print("The load is : ", load1)

        
    # part 2
    part2_map = char_map.copy()
    number_of_cycles = int(2e2)
    load_history = np.zeros(number_of_cycles)
    for i in range(number_of_cycles):
        for j in range(4):
            for k in range(part2_map.shape[1]):
                part2_map[:,k] = pushNorth(part2_map[:,k])
            part2_map = np.rot90(part2_map,-1)
        load_history[i] = calculateLoad(part2_map)
            
        if i % 100 == 0:
            print("i = ", i)
    
    plt.figure(dpi=300)
    # plt.plot(np.arange(325,340),load_history[325:340])
    plt.plot(load_history[101:186])
    plt.xlabel("Number of cycles")
    plt.ylabel("Load")
    # plt.ylim(107211,107215)
    plt.title("Load history")
    plt.grid()
    plt.savefig("load_history.png")

    # notice that the load is periodic every 85 cycles, so we can calculate the load at 1e9 - 1 - 85 * const, where const is some number. In this case, const = 11764704, which gives 159
    print("Load at 159 = ", load_history[159])