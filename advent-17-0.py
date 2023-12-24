import numpy as np
import heapq as hq

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-17-tst.txt"

def manhattanDistanceToEnd(current_location : tuple, end : tuple) -> int:
    # print("current_location: ", current_location)
    # print("end: ", end) 
    return abs(current_location[0] - end[0]) + abs(current_location[1] - end[1])

def takeNextStep(last_location : tuple, current_location : tuple, bounds : tuple, straight_counter : int) -> list[tuple[tuple, int]]:
    """Return a list of possible next steps"""

    next_location = [tuple(np.add(current_location, (-1,0))), tuple(np.add(current_location, (1,0))), tuple(np.add(current_location, (0,1))), tuple(np.add(current_location, (0,-1)))]

    # remove any out of bounds locations
    for i in range(len(next_location)-1,-1,-1):
        if (next_location[i][0] < 0) or (next_location[i][0] > bounds[0]) or (next_location[i][1] < 0) or (next_location[i][1] > bounds[1]):
            next_location.pop(i)
    
    # remove the last location, no backtracking
    next_location.remove(last_location)

    list_of_next_locations = []
    # print("next_location: ", next_location)
    # check for long straight line condition
    i = 0
    while i < len(next_location):
        current_counter = straight_counter
        if np.any(np.abs(np.subtract(next_location[i], last_location)) == 2):
            current_counter += 1
            if current_counter > 2:
                i += 1
                continue # if the straight counter exceeds 3, skip this location
            list_of_next_locations.append(tuple([next_location[i], current_counter]))
        else:
            current_counter = 0
            list_of_next_locations.append(tuple([next_location[i], current_counter]))
        i += 1

    return list_of_next_locations
    
def computeLoss(map : np.ndarray, current_loss : int, next_location : tuple) -> int:
    """Compute the loss of the current location"""
    return current_loss + int(map[next_location])

def pseudoLoss(loss, distance):
    """Compute the pseudo loss"""
    return loss**2 + distance*3

def main():
    # read in the map
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")

    # convert map to numpy array
    int_map = np.zeros([len(input_file),len(input_file[0])],dtype=int)
    for l, line in enumerate(input_file):
        int_map[l,:] = np.array([int(i) for i in line.strip("\n")])

    # print("char_map: \n", int_map)

    # start = (0,0)
    end = (int_map.shape[0]-1, int_map.shape[1]-1)

    # set of visited locations
    visited_locations = list()
    visited_locations.append([(0,0),1]) # location and number of times visited

    visited_locations.append([(1,0),1])
    visited_locations.append([(0,1),1])
    # print("visited_locations: ", visited_locations)

    stack = []
    stack.append((int_map[0,1], 0, [(0,0),(0,1)]))
    stack.append((int_map[1,0], 0, [(0,0),(1,0)])) # values: loss, pseudo-loss, straight_counter, sequence of steps
    

    # print("stack: ", stack)

    hq.heapify(stack)
    # print("stack after heapify: ", stack)

    # evolve the stack
    iterations = 0
    while True:
        
        # check if we have reached the end
        first_sequence_in_stack = stack[0][-1]
        # print("Last location : ", first_sequence_in_stack[-1])
    
        if (first_sequence_in_stack[-1][0] == end[0]) and (first_sequence_in_stack[-1][1] == end[1]):
        # if visited_locations[-1][0] == end and visited_locations[-1][1] == 2:
            print("Reached the end!")
            print("The shortest path is: ", first_sequence_in_stack)
            print("locations visited: ", visited_locations[-1][0], visited_locations[-1][1])

            loss_at_end = []
            for i in first_sequence_in_stack[1:]:
                # print("i: ", i, flush=True)
                loss_at_end.append(int_map[i])
            print("loss at end: ", loss_at_end)
            print("The total loss at end is: ", sum(loss_at_end))


            # print("The loss is: ", stack[0][0]) # 1641

            break

        # get the next locations
        list_of_next_locations = takeNextStep(last_location=first_sequence_in_stack[-2], current_location=first_sequence_in_stack[-1], bounds=end, straight_counter=stack[0][1])

        # exclude the locations that have been visited
        for i in range(len(list_of_next_locations)-1,-1,-1):
            break_flag = False
            for j in range(len(visited_locations)):
                if list_of_next_locations[i][0] == visited_locations[j][0]:
                    # if list_of_next_locations[i][0] != end:
                    #     list_of_next_locations.pop(i)
                    #     break_flag = True
                    #     break
                    if visited_locations[j][1] > 1:
                        list_of_next_locations.pop(i)
                        break_flag = True
                        break
                    else:
                        visited_locations[j][1] += 1
                        break_flag = True
                        break
            if break_flag:
                break
            visited_locations.append([list_of_next_locations[i][0],1])

        # update loss for each next location
        # update the manhattan distance to end for each next location
        list_of_losses = []
        # list_of_manhattan_distances = []
        list_of_straight_counters = []
        # list_of_pseudo_losses = []
        for next_location in list_of_next_locations:
            list_of_straight_counters.append(next_location[1])
            this_loss = computeLoss(map=int_map, current_loss=stack[0][0], next_location=next_location[0])
            # this_distance = manhattanDistanceToEnd(current_location=next_location[0], end=end)
            
            list_of_losses.append(this_loss)
            # list_of_manhattan_distances.append(this_distance)
            # list_of_pseudo_losses.append(pseudoLoss(this_loss, this_distance))


        # remove the first element in the stack because it has been used
        hq.heappop(stack)

        # add the next locations to the stack
        for i, next_location in enumerate(list_of_next_locations):
            hq.heappush(stack, (list_of_losses[i], list_of_straight_counters[i], first_sequence_in_stack + [next_location[0]]))
        
        iterations += 1
        if iterations % 1000000 == 0:
            print("iterations: ", iterations)
            # print("visited_locations: ", visited_locations)
            # print("first key in stack: ", first_sequence_in_stack)
            print("first in stack: ", stack[0])
            print("\n")
            


if __name__ == "__main__":
    main()


