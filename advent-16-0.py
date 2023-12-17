import numpy as np

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-16-0.txt"

guide = dict()
guide["|"] = np.array([[-1,0], [1,0]])
guide["-"] = np.array([[0,-1], [0,1]])
guide["\\"] = np.array([[1,1],[-1,-1]])
guide["/"] = np.array([[-1,1],[1,-1]])
guide["."] = np.array([0,0])

def nextTile(current_location, outgoing_direction):
    """Vector sum of location and direction gives the next location"""
    if outgoing_direction[0] != 0 and outgoing_direction[1] != 0:
        raise ValueError("Direction must be one of four cardinal directions, not diagonal")
    
    return current_location + outgoing_direction

def vectorizeDirection(current_location, incoming_direction, symbol):
    """Iterate through the possible next locations given the current location and last location"""
    current_symbol = symbol

    # first element is always the row, second element is always the column
    if current_symbol == ".": # empty space; keep going in the same direction
        outgoing_direction = incoming_direction
        # print("outgoing_direction: ", outgoing_direction)
        return (nextTile(current_location, outgoing_direction), outgoing_direction)
    if current_symbol == "-":
        if incoming_direction[0] == 0: # moving horizontally
            outgoing_direction = incoming_direction
            # print("outgoing_direction: ", outgoing_direction)
            return (nextTile(current_location, outgoing_direction), outgoing_direction)
        else: # moving vertically
            outgoing_direction = [guide[current_symbol][0,:], guide[current_symbol][1,:]]
            # print("outgoing_direction: ", outgoing_direction)
            return [(nextTile(current_location, outgoing_direction[i]), outgoing_direction[i]) for i in range(2)]
    elif current_symbol == "|":
        if incoming_direction[0] == 1: # moving vertically
            outgoing_direction = incoming_direction
            # print("outgoing_direction: ", outgoing_direction)
            return (nextTile(current_location, outgoing_direction), outgoing_direction)
        else: # moving horizontally
            outgoing_direction = [guide[current_symbol][0,:], guide[current_symbol][1,:]]
            # print("outgoing_direction: ", outgoing_direction)
            return [(nextTile(current_location, outgoing_direction[i]), outgoing_direction[i]) for i in range(2)]
    elif current_symbol == "\\":
        outgoing_direction = guide[current_symbol] - incoming_direction
        for i in range(2):
            if np.any(outgoing_direction[i] == 0):
                outgoing_direction = outgoing_direction[i]
                break
        # print("outgoing_direction: ", outgoing_direction)
        return (nextTile(current_location, outgoing_direction), outgoing_direction)
    elif current_symbol == "/":
        outgoing_direction = guide[current_symbol] - incoming_direction
        for i in range(2):
            if np.any(outgoing_direction[i] == 0):
                outgoing_direction = outgoing_direction[i]
                break
        # print("outgoing_direction: ", outgoing_direction)
        return (nextTile(current_location, outgoing_direction), outgoing_direction)
    else:
        raise ValueError("Invalid symbol")
    
def determineEnergizedTiles(char_map, start):
    # iterate through the map
    rays = [start]
    location_and_direction_history = set()
    location_and_direction_history.add((tuple(start[0]),tuple(start[1])))
    while len(rays) > 0:
        # print("--------------------")
        # # print("rays: ", rays)
        new_rays = []
        for ray in rays:
            # # print("ray: ", ray)
            current_location = ray[0]
            incoming_direction = ray[1]
            current_symbol = char_map[current_location[0], current_location[1]]
            # print("current_symbol: ", current_symbol)
            next_tile = vectorizeDirection(current_location, incoming_direction, current_symbol)
            # print("next_tile: ", next_tile)

            if type(next_tile) is list:
                new_rays.append(next_tile[0])
                new_rays.append(next_tile[1])
            else:
                new_rays.append(next_tile)

        # print("new_rays: ", new_rays)
        nray_index = 0
        while nray_index < len(new_rays):
            nray = new_rays[nray_index]
            # print("Considering ray: ", nray)
            if 0 > nray[0][0] or char_map.shape[0] <= nray[0][0]:
                # print("ray {} is out of bounds".format(nray))
                new_rays.pop(nray_index)
            elif 0 > nray[0][1] or char_map.shape[1] <= nray[0][1]:
                # print("ray {} is out of bounds".format(nray))
                new_rays.pop(nray_index)
            elif (tuple(nray[0]),tuple(nray[1])) in location_and_direction_history:
                # print("ray {} is already in location_history ten times".format(nray))
                new_rays.pop(nray_index)
            else:
                nray_index += 1
        # print("new_rays after cleaning: ", new_rays)
    
        for lray in new_rays:
            location_and_direction_history.add((tuple(lray[0]),tuple(lray[1])))
        rays = new_rays

    # print("location_and_direction_history: ", location_and_direction_history)

    # print("Number of energized tiles = ", len(location_history))

    energized_map = np.zeros(char_map.shape, dtype=int)
    for location_and_direction in location_and_direction_history:
        energized_map[location_and_direction[0][0], location_and_direction[0][1]] = 1

    return energized_map

def main():
    # read in the map
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")

    # convert map to numpy array
    char_map = np.chararray((len(input_file),len(input_file[0])),unicode=True)
    for l, line in enumerate(input_file):
        char_map[l] = np.array([i for i in line.strip("\n")])

    start = (np.array([0,0]), np.array([0,1])) # starts at top-left, moving right

    # print("char_map: \n", char_map)
    # print("start: ", start)

    print("Part 1")
    print("Number of energized tiles = ", np.sum(determineEnergizedTiles(char_map, start))) #8146


    # Part 2

    starting_locations_and_direction = []
    
    # top row, go down
    i = 0
    for j in range(char_map.shape[1]):
        starting_locations_and_direction.append((np.array([i, j]), np.array([1,0])))
    
    # bottom row, go up
    i = char_map.shape[0]-1
    for j in range(char_map.shape[1]):
        starting_locations_and_direction.append((np.array([i, j]), np.array([-1,0])))
    
    # left column, go right
    j = 0
    for i in range(char_map.shape[0]):
        starting_locations_and_direction.append((np.array([i, j]), np.array([0,1])))
    
    # right column, go left
    j = char_map.shape[1]-1
    for i in range(char_map.shape[0]):
        starting_locations_and_direction.append((np.array([i, j]), np.array([0,-1])))

    print("Part 2")
    print("There are {} starting locations and directions".format(len(starting_locations_and_direction)))

    number_of_energized_tiles_per_config = []
    for starting_location_and_direction in starting_locations_and_direction:
        number_of_energized_tiles_per_config.append(np.sum(determineEnergizedTiles(char_map, starting_location_and_direction)))

    print("Max number of energized tiles = ", np.max(number_of_energized_tiles_per_config)) #8385
            
if __name__ == "__main__":
    main()