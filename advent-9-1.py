#NOTE: Solution does not give exact answer because of rounding errors from the polynomial fit. Check advent-9-0.py for the exact solution.

import numpy as np
import numpy.polynomial.polynomial as poly

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-9-0.txt"

def find_polynomial(ycoords):
    xcoords = np.arange(1,len(ycoords)+1)

    power = 0
    resid = 1

    while resid != 0:
        # resid_before = resid
        coeffs, extra_info =  poly.polyfit(xcoords, ycoords, power, full=True)
        # print("\n")
        # print(extra_info[0])
        if extra_info[0].size == 0:
            resid = 0
        else:
            resid = float(extra_info[0][0])
        rank = int(extra_info[1])
        power += 1

    return coeffs, rank

def find_next_instance(ycoords, coeffs, reverse=False):
    
    if reverse:
        xcoords = 0
    else:
        xcoords = len(ycoords)+1
    
    next_instance = poly.polyval(xcoords, coeffs)

    return next_instance

if __name__ == "__main__":
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")

    next_instance_array = np.empty(len(input_file))
    for l, line in enumerate(input_file):
        ycoords = np.array([int(i) for i in line.strip().split()])
        print("ycoords : ", ycoords)
        coeffs, rank = find_polynomial(ycoords)
        print("n : ", len(coeffs))
        # print(coeffs)
        next_instance = find_next_instance(ycoords, coeffs)
        print("Next instance : ", next_instance)
        next_instance_array[l] = next_instance
        # zeroth_instance = find_next_instance(ycoords, coeffs, reverse=True)
        # print("Next instance : ", int(round(zeroth_instance,0)))

    print("Total of all next instances : ", np.sum(next_instance_array))

    # 2098530125