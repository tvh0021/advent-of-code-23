import numpy as np

file_path = "input-22-0.txt"

def findBrickAtHeight(xyslice : np.ndarray):
    """Find the brick at the given height"""
    nx, ny = xyslice.shape
    bricks_at_height = set()

    for x in range(nx):
        for y in range(ny):
            if xyslice[x,y] != -1 and xyslice[x,y] not in bricks_at_height:
                bricks_at_height.add(xyslice[x,y])
    
    return bricks_at_height

def checkCanFall(xy_slice_top : np.ndarray, xy_slice_bottom : np.ndarray, bricks_at_height : set):
    """Check if the brick can fall"""
    
    list_of_bricks_to_check = []
    list_of_yes_no = []

    for brick in bricks_at_height:
        list_of_bricks_to_check.append(brick)
        # if all the spaces below the brick are empty, then it can fall
        if np.all(xy_slice_bottom[np.where(xy_slice_top == brick)] == -1):
            list_of_yes_no.append(True)
        else:
            list_of_yes_no.append(False)
    
    return (list_of_bricks_to_check, list_of_yes_no)
            

def gravity(domain : np.ndarray, number_of_falling_bricks : int = np.inf):
    """Apply gravity to the domain"""

    nx, ny, nz = domain.shape
    bricks_fell_this_round = 0

    for z in range(2, domain.shape[2]):
        xy_slice = domain[:,:,z]
        xy_slice_below = domain[:,:,z-1]

        # find the bricks at this z level
        bricks_at_z = findBrickAtHeight(xy_slice)
        
        # for each brick at this z level, check if it can fall
        list_of_bricks_to_check, list_of_yes_no = checkCanFall(xy_slice, xy_slice_below, bricks_at_z)

        # move the bricks that can fall down one level
        for i, brick in enumerate(list_of_bricks_to_check):
            if list_of_yes_no[i]:
                # move the brick down one level
                xy_slice_below[np.where(xy_slice == brick)] = brick
                xy_slice[np.where(xy_slice == brick)] = -1
                bricks_fell_this_round += 1
    
    number_of_falling_bricks = bricks_fell_this_round
    
    # move the bricks down one height level at a time until no more bricks can fall
    while number_of_falling_bricks != 0:
        domain, number_of_falling_bricks = gravity(domain, number_of_falling_bricks)

    return domain, number_of_falling_bricks
        


def main():
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        # lines now contains each line from the file as a string

    # print("lines: ", lines)

    # convert the lines to a numpy array
    bricks = np.zeros((len(lines), 6), dtype=int)
    number_of_bricks = len(lines)
    for i, line in enumerate(lines):
        line = line.replace("~", ",")
        bricks[i] = np.array([int(j) for j in line.split(",")])
    
    # print("bricks: ", bricks)
    print("The number of bricks is : ", number_of_bricks)

    # create a meshgrid that encompasses the entire domain, then fill it with values of the bricks

    # max of each dimension is the futhermost brick in that dimension
    nx = np.max(bricks[:,3])+1
    ny = np.max(bricks[:,4])+1
    nz = np.max(bricks[:,5])+1

    domain = np.ones((nx,ny,nz), dtype=int) * -1

    # fill the domain with the bricks
    for i, brick in enumerate(bricks):
        domain[brick[0]:brick[3]+1, brick[1]:brick[4]+1, brick[2]:brick[5]+1] = i

    # print("domain xz: \n", np.flipud(domain[:,0,:].T))
    # print("domain yz: \n", np.flipud(domain[0,:,:].T))
        

    # apply gravity
    domain_after_gravity, *k = gravity(domain)

    # print("domain xz after gravity: \n", np.flipud(domain_after_gravity[:,0,:].T))
    # print("domain yz after gravity: \n", np.flipud(domain_after_gravity[0,:,:].T))
    
    # now reiterate through the domain and note down which bricks are supported by which bricks
    
    bricks_supported_by = {i:[] for i in range(number_of_bricks)}
    
    for z in range(2,domain_after_gravity.shape[2]):
        if np.all(domain_after_gravity[:,:,z] == -1):
            # print("z = ", z, " is empty. This should not happen.")
            continue
        else:
            slice_here = domain_after_gravity[:,:,z]
            slice_below = domain_after_gravity[:,:,z-1]
            
            # find the bricks at this z level
            bricks_at_z = findBrickAtHeight(slice_here)
            # print("bricks at z = ", z, " are : ", bricks_at_z)
            # for each brick at this z level, check how many bricks are immediately below it
            # if there is only one brick below it, then it is supported by only one brick
            
            for brick in bricks_at_z:
                location_below_brick = slice_below[np.where(slice_here == brick)]
                supports_below = np.unique(location_below_brick)
                bricks_supported_by[brick].extend(supports_below.tolist())
                    
    # print("bricks supported by : ", bricks_supported_by)    
            
    # first, get rid of empty spaces and bricks supporting themselves
    for i in range(number_of_bricks):
        bricks_supported_by[i] = [j for j in bricks_supported_by[i] if j != -1 and j != i]
        
    # print("bricks supported by : ", bricks_supported_by)
    
    # look at the list, find the critical bricks that will cause the tower to collapse if they are removed
    critical_bricks = set()
    for i in range(number_of_bricks):
        if len(bricks_supported_by[i]) == 1:
            critical_bricks.add(bricks_supported_by[i][0])

    print("critical bricks : ", critical_bricks)
    
    # lastly, the leftover bricks are the ones that cannot be disintergrated safely
    leftover_bricks = set(range(number_of_bricks)) - critical_bricks
    
    print("leftover bricks : ", leftover_bricks)
    print("The number of leftover bricks is : ", len(leftover_bricks))
            
    
    return None
        
    
if __name__ == "__main__":
    main()
    