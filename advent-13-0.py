import numpy as np

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-13-0.txt"

def isReflection(map, row=None, col=None, part=1):
    width = map.shape[1]
    height = map.shape[0]

    if row is None and col is None:
        return 0
    elif row is None:
        # print("col = ", col)
        if col <= width / 2:
            num_cols = col
            compare_array = np.char.compare_chararrays(map[:,:num_cols], np.fliplr(map[:,num_cols:2*num_cols]), "==", True)
            if part == 1:
                if compare_array.all() == True:
                    # print("col ", col, " reflection : ", compare_array)
                    return col
                else:
                    return 0
            else:
                # print("Diagnostic")
                # print(compare_array)
                # print(compare_array.size)
                # print(np.sum(compare_array))
                if compare_array.size - np.sum(compare_array) == 1: # if only one element is different, then this is the smudge
                    return col
                else:
                    return 0
        else:
            num_cols = width - col
            compare_array = np.char.compare_chararrays(map[:,col-num_cols:col], np.fliplr(map[:,col:]), "==", True)
            if part == 1:
                if compare_array.all():
                    # print("col ", col, " reflection : ", compare_array)
                    return col
                else:
                    return 0
            else:
                # print("Diagnostic")
                # print(compare_array)
                # print(compare_array.size)
                # print(np.sum(compare_array))
                if compare_array.size - np.sum(compare_array) == 1: # if only one element is different, then this is the smudge
                    return col
                else:
                    return 0
    elif col is None:
        # print("row = ", row)
        if row <= height / 2:
            num_rows = row
            compare_array = np.char.compare_chararrays(map[:num_rows,:], np.flipud(map[num_rows:2*num_rows,:]), "==", True)
            if part == 1:
                if compare_array.all() == True:
                    # print("row ", row, " reflection : ", compare_array)
                    return row
                else:
                    return 0
            else:
                # print("Diagnostic")
                # print(compare_array)
                # print(compare_array.size)
                # print(np.sum(compare_array))
                if compare_array.size - np.sum(compare_array) == 1: # if only one element is different, then this is the smudge
                    return col
                else:
                    return 0
        else:
            num_rows = height - row
            # print(map[row-num_rows:row,:])
            # print(np.flip(map[row:,:], axis=0))
            compare_array = np.char.compare_chararrays(map[row-num_rows:row,:], np.flipud(map[row:,:]), "==", True)
            if part == 1:
                if compare_array.all() == True:
                    # print("row ", row, " reflection : ", compare_array)
                    return row
                else:
                    return 0
            else:
                # print("Diagnostic")
                # print(compare_array)
                # print(compare_array.size)
                # print(np.sum(compare_array))
                if compare_array.size - np.sum(compare_array) == 1: # if only one element is different, then this is the smudge
                    return col
                else:
                    return 0
    else:
        print("Error in isReflection. row and col cannot both be specified.")
        return None

if __name__ == "__main__":
    # read in the map
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")

    # list of lists, each list is a section of the map
    symbol_map = []
    last_row = 0
    for l, line in enumerate(input_file):
        if len(line) == 0:
            symbol_map.append(input_file[last_row:l])
            last_row = l + 1
        if l == len(input_file) - 1:
            symbol_map.append(input_file[last_row:])

    # print(symbol_map[1])

    # Part 1
    # scan through each map section and find the reflections
    row_reflection = []
    col_reflection = []
    for section in symbol_map:
        char_map = np.chararray((len(section),len(section[0])),unicode=True)
        for l, line in enumerate(section):
            char_map[l] = np.array([i for i in line])
        
        # print(char_map)
        found_reflection = False
        for row in range(1,char_map.shape[0]):
            if isReflection(char_map, row=row, part=1) != 0:
                # print("Reflection at row ", row)
                row_reflection.append(row)
                found_reflection = True
                break
        # if no reflection is found in the rows, check the columns
        if not found_reflection:
            for col in range(1,char_map.shape[1]):
                if isReflection(char_map, col=col, part=1) != 0:
                    # print("Reflection at column ", col)
                    col_reflection.append(col)
                    found_reflection = True
                    break
            
    print("Part 1")
    print("Total reflection = ", sum(row_reflection) * 100 + sum(col_reflection))


    # Part 2
    # scan through each map section and find the smudge
    row_reflection = []
    col_reflection = []
    for section in symbol_map:
        char_map = np.chararray((len(section),len(section[0])),unicode=True)
        for l, line in enumerate(section):
            char_map[l] = np.array([i for i in line])
        
        # print(char_map)
        found_smudge = False
        for row in range(1,char_map.shape[0]):
            if isReflection(char_map, row=row, part=2) != 0:
                # print("Reflection at row ", row)
                row_reflection.append(row)
                found_smudge = True
                break
        # if no reflection is found in the rows, check the columns
        if not found_smudge:
            for col in range(1,char_map.shape[1]):
                if isReflection(char_map, col=col, part=2) != 0:
                    # print("Reflection at column ", col)
                    col_reflection.append(col)
                    found_smudge = True
                    break

    print("Part 2")
    print("Total reflection with smudges = ", sum(row_reflection) * 100 + sum(col_reflection))

    