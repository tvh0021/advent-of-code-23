import numpy as np
import sys
sys.setrecursionlimit(1000000)
np.set_printoptions(threshold=sys.maxsize)

from collections import deque

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-10-0.txt"
      
def Iterator(char_map, current_location):
    """Iterate through the possible next locations given the current location

    Args:
        char_map (2d chararray): the entire map
        current_location (1d array): the current location

    Returns:
        list[1d array]: a list of possible next locations
    """
    current_symbol = char_map[current_location[0],current_location[1]]

    # first element is always the row, second element is always the column
    if current_symbol == "S":
        return [np.array([-1,0]), np.array([1,0]), np.array([0,-1]), np.array([0,1])]
    elif current_symbol == "|":
        return [np.array([-1,0]), np.array([1,0])]
    elif current_symbol == "-":
        return [np.array([0,-1]), np.array([0,1])]
    elif current_symbol == "L":
        return [np.array([-1,0]), np.array([0,1])]
    elif current_symbol == "J":
        return [np.array([-1,0]), np.array([0,-1])]
    elif current_symbol == "7":
        return [np.array([0,-1]), np.array([1,0])]
    elif current_symbol == "F":
        return [np.array([0,1]), np.array([1,0])]
    elif current_symbol == ".":
        return []

def findFirstBranch(char_map, start_location):
    """Find the first branch of the pipe

    Args:
        char_map (2d chararray): the entire map
        start_location (1d array): location of "S"

    Returns:
        1d array, list[1d array]: the starting point, and the two next locations
    """

    final_location = [] # there are exactly two pipes that are connected to the starting point
    print("The starting point is : ", char_map[start_location[0],start_location[1]])

    for i in range(-1 if start_location[0] > 0 else 0, 2 if start_location[0] < char_map.shape[0]-1 else 1):
        for j in range(-1 if start_location[1] > 0 else 0, 2 if start_location[1] < char_map.shape[1]-1 else 1):
            # print("Considering : ", char_map[start_location[0]+i,start_location[1]+j])
            connected_nodes = Iterator(char_map, start_location + np.array([i,j]))
            double_connected = [not (next_node + np.array([i,j])).any() for next_node in connected_nodes]
            # print(double_connected)
            
            if any(double_connected):
                final_location.append(start_location + np.array([i,j]))

    print("First branch includes : ", [char_map[final_location[0][0],final_location[0][1]], char_map[final_location[1][0],final_location[1][1]]])

    return start_location, final_location

def findNextLocation(char_map, current_location, previous_location, depth=1, previous_location_list=[]):
    """Recursively search for the next pipe until the "S" is found again

    Args:
        char_map (2d chararray): the entire map
        current_location (1d array): the current location
        previous_location (1d array): the previous location, used to determine the next location
        depth (int, optional): Recursive depth, also tracks the length of the pipe. Defaults to 1.
        previous_location_list (list, optional): list of all locations of pipe segments. Defaults to [].
    """
    
    # obtain the shape of the current pipe, then ignore the end that is connected to the previous pipe
    connected_nodes = Iterator(char_map, current_location)
    # print("Connected nodes : ", connected_nodes)    
    double_connected = [(next_node + (current_location - previous_location)).any() for next_node in connected_nodes]

    # print("Connected to previous location : ", double_connected)
    
    for i in range(2):
        if double_connected[i]:
            next_location = current_location + connected_nodes[i]
            previous_location_list.append(current_location)
            # print("Next symbol : ", char_map[next_location[0],next_location[1]])
            if char_map[next_location[0],next_location[1]] == "S":
                depth = depth + 1
                print("Found the end of the loop!")
                print("The number of steps is : ", depth)
                print("The number of steps to reach the furthest location is : ", depth/2)
                break
            else:
                findNextLocation(char_map, next_location, current_location, depth=depth+1, previous_location_list=previous_location_list)
            break
    
    return

def isPointInLoop(x: int, y: int, poly: list[tuple[int, int]]) -> bool:
    """Determine if the point is enclosed within the loop. Taken from Wikipedia article on Even-Odd Rule, modified slightly.

    Args:
      x -- The x coordinates of point.
      y -- The y coordinates of point.
      poly -- a list of tuples [(x, y), (x, y), ...]

    Returns:
      True if the point is inside the loop, False if not"""
    num = len(poly)
    j = num - 1
    c = False
    for i in range(num):
        if (x == poly[i][0]) and (y == poly[i][1]):
            # point is a corner
            return False
        if (poly[i][1] > y) != (poly[j][1] > y):
            slope = (x - poly[i][0]) * (poly[j][1] - poly[i][1]) - (
                poly[j][0] - poly[i][0]
            ) * (y - poly[i][1])
            if slope == 0:
                # point is on boundary
                return False
            if (slope < 0) != (poly[j][1] < poly[i][1]):
                c = not c
        j = i
    return c

def castHorizontalRay(char_map, symbol_to_consider):
    """Using the ray casting algorithm, determine if a dot is enclosed by the pipe. If a dot is inside the pipe, there will be a 

    Args:
        char_map (_type_): _description_
        symbol_to_consider (_type_): _description_
    """

if __name__ == "__main__":
    # read in the map
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")

    # make a numpy chararray of the map
    char_map = np.chararray((len(input_file),len(input_file[0])),unicode=True)
    for l, line in enumerate(input_file):
        char_map[l] = np.array([i for i in line.strip("\n")])
    print(char_map) 

    # Find the starting point
    starting_point = np.array([0,0])
    starting_point_found = False
    for l, line in enumerate(char_map):
        for c, char in enumerate(line):
            if char == "S":
                starting_point = np.array([l,c])
                starting_point_found = True
                break
        if starting_point_found:
            break
    print("Starting point is at coordinates : ", starting_point)

    # search in the neighborhood of the starting point for the next pipe
    print("The neighborhood of the starting point is : \n", char_map[starting_point[0]-1:starting_point[0]+2,starting_point[1]-1:starting_point[1]+2])

    # Iterate through the loop
    starting_point, branches = findFirstBranch(char_map, starting_point)

    # choose one of the branches, recursively search for the next pipe until the "S" is found again
    previous_location_list = [starting_point]
    findNextLocation(char_map, branches[0], starting_point, depth=1, previous_location_list=previous_location_list)

    print("All pipe locations : ", len(previous_location_list))
    # print(previous_location_list[0])
    # print(previous_location_list[-1])
    
    # replace all non-pipes with dots and print the map
    pipe_map = np.empty(char_map.shape, dtype=str)
    pipe_map[:] = 0
    for n in range(len(previous_location_list)):
        pipe_map[previous_location_list[n][0],previous_location_list[n][1]] = char_map[previous_location_list[n][0],previous_location_list[n][1]]

    list_of_points_in_pipe = []
    for location in previous_location_list:
        list_of_points_in_pipe.append(tuple(location))

    print("Points in pipe as a list of tuples : ", list_of_points_in_pipe[:10])

    # make four numbers that define the bounding box of the pipe, slightly save computational time by only checking the points within the bounding box
    bounding_box = [np.min(np.array(list_of_points_in_pipe), axis=0), np.max(np.array(list_of_points_in_pipe), axis=0)]
    print("Bounding box : ", bounding_box[0])
    print("Bounding box : ", bounding_box[1])

    # test if a point is enclosed by the pipe
    total_enclosed = 0
    for l in range(bounding_box[0][0], bounding_box[1][0]):
        print("Scanning line ", l)
        for c in range(bounding_box[0][1], bounding_box[1][1]):
            if isPointInLoop(l,c,list_of_points_in_pipe):
                pipe_map[l,c] = "I"
                total_enclosed += 1

    print("Total enclosed : ", total_enclosed)