import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-11-0.txt"
number_to_multiply = 1000000

def computeManhattanPairwiseDistance(x, y):
    """Sume of two-point Manhattan distance function

    Args:
        x (1d array): x coordinates of the points
        y (1d array): y coordinates of the points

    Returns:
        int: sum of the pairwise Manhattan distances
    """
    xa = np.reshape(x, (len(x),1))
    xb = np.reshape(x, (1,len(x)))
    ya = np.reshape(y, (len(y),1))
    yb = np.reshape(y, (1,len(y)))
    
    pairwise_diffs = np.abs(xa - xb) + np.abs(ya - yb)
    
    # take the upper triangle of the matrix to avoid double counting
    pairwise_diffs = np.triu(pairwise_diffs)
    
    return np.sum(pairwise_diffs)

if __name__ == "__main__":
    # read in the map
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")

    # make a numpy chararray of the map
    char_map = np.chararray((len(input_file),len(input_file[0])),unicode=True)
    for l, line in enumerate(input_file):
        char_map[l] = np.array([i for i in line.strip("\n")])
    # print("Text to numpy map : \n", char_map)
    
    # convert char_map to a numpy array of 1s and 0s
    bool_map = np.where(char_map == '.', 0, 1)
    
    # extract all the positions of the ones in the bool_map
    positions = np.where(bool_map == 1)
    
    row_positions = positions[0]
    # print("Row positions of galaxies : ", row_positions[300:350])
    col_positions = positions[1]
    
    print("Number of galaxies : ", len(row_positions))
    
    # sum up the pairwise differences to obtain the total Manhattan distance between the galaxies
    print("Total Manhattan distance before modification : ", computeManhattanPairwiseDistance(row_positions, col_positions))
    
    # now go through rows and columns in the list of galaxy positions and see if there are any missing rows or columns
    unique_rows = np.unique(row_positions)
    unique_cols = np.unique(col_positions)
    
    all_rows = np.arange(0, bool_map.shape[0])
    all_cols = np.arange(0, bool_map.shape[1])
    
    missing_rows = np.setdiff1d(all_rows, unique_rows)
    missing_cols = np.setdiff1d(all_cols, unique_cols)
    
    # append the length of the total number of rows or columns to the end of the missing rows or columns list to avoid index out of bounds errors
    missing_rows = np.append(missing_rows, len(all_rows))
    missing_cols = np.append(missing_cols, len(all_cols))
    # print("Missing rows : ", missing_rows)
    # print("Missing cols : ", missing_cols)
    
    # iterate through the rows and columns of the galaxy positions and add n number of rows or columns accordingly
    number_to_add = number_to_multiply - 1
    
    number_of_misses = 0
    row_positions_after = row_positions.copy()
    
    for i, row in enumerate(row_positions):
        if row > missing_rows[number_of_misses]:
            # print("Row {} is greater than missing row {}".format(row, missing_rows[number_of_misses]))
            # print("Adding {} to each row after".format(number_to_add, row))
            row_positions_after[i:] += number_to_add
            number_of_misses += 1
    # print("Row positions of galaxies after modification: ", row_positions_after)
    
    number_of_misses = 0
    # sort the col positions so that the indices are in order
    col_positions_sort_index = np.argsort(col_positions)
    col_positions_sort = col_positions[col_positions_sort_index]
    col_positions_after_sort = col_positions_sort.copy()
    # col_positions_after = col_positions_after[col_positions_after_sort_index]

    for j, col in enumerate(col_positions_sort):
        if col > missing_cols[number_of_misses]:
            # print("Col {} is greater than missing col {}".format(col, missing_cols[number_of_misses]))
            # print("Adding {} to each col after".format(number_to_add, col))
            col_positions_after_sort[j:] += number_to_add
            number_of_misses += 1
            
    col_positions_after = col_positions_after_sort[np.argsort(col_positions_sort_index)]
    # print("Col positions of galaxies after modification: ", col_positions_after)
    
    print("Total Manhattan distance after modification : ", computeManhattanPairwiseDistance(row_positions_after, col_positions_after))
    
            
            
    
    