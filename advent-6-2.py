import numpy as np

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-6-0.txt"

def calculate_distance(total_time, time_held):
    """Calculate the distance travelled at a given hold-down time.

    Args:
        total_time (int): The time of the race
        time_held (int): The time you hold down the button

    Returns:
        int: The distance travelled
    """
    return (total_time - time_held) * time_held

if __name__ == "__main__":
    with open(file_path, "r") as f:
        input = np.empty((2,1),dtype=int)

        row = 0
        for line in f:
            input[row,0] = "".join((line.split(":")[1]).split())
            row += 1

    print(input)

    # make an array of zeros corresponding to the number of seconds in the game
    distance_keeper = np.zeros(shape=(input.shape[1],max(input[0,:])+1),dtype=int)
    print(distance_keeper.shape)

    # populate the time_keeper array by calculating the different combinations of times and velocity
    for i, n in enumerate(input[0,:]):
        possible_time_held = np.arange(0,n+1)
        total_time = np.ones(len(possible_time_held)) * n
        pad_width = distance_keeper.shape[1] - len(possible_time_held)
        distance_keeper[i,:] = np.pad(calculate_distance(total_time, possible_time_held), pad_width=(0,pad_width), mode='constant', constant_values=0)

    configurations = np.zeros(len(input[0,:]))
    for i in range(distance_keeper.shape[0]):
        configurations[i] = (distance_keeper[i,:] > input[1,i]).sum()

    print("Number of configurations for each time : ", configurations)
    print("Total number of configurations :", configurations.prod())