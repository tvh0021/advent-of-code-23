
if __name__ == "__main__":
    with open("input-5-0.txt") as f:
        seeds = f.readline().strip("seeds: ").strip("\n").split()
        
        seed_ranges = []
        total_number_of_seeds = 0
        # convert the seed ranges into segments of seed. [start, end) (end is not included)
        for i in range(0,len(seeds),2):
            seed_ranges.append([int(seeds[i]), int(seeds[i+1]) + int(seeds[i])])
            total_number_of_seeds += int(seeds[i+1])
            
        print("Seed ranges : ", seed_ranges)
        
        print("Total number of seeds : ", total_number_of_seeds)
        
        
        
        mapping = dict()
        
        # this part converts all the lines into a dict
        for line in f:
            if line == "\n":
                continue
            else:
                line = line.strip("\n")
                if not line[0].isnumeric():
                    key_name = line.strip(" map:")
                    mapping[key_name] = []
                else:
                    mapping[key_name].append([int(line.split(" ")[i]) for i in range(3)])
        
        # print("Keys : ", mapping.keys())
        # print("\n")
        # print("Mapping : ", mapping)
        
        
        # now iterate through the seeds and find if the seed falls within the range of any of the maps, otherwise map it one-to-one
        seeds_mapped_to_location = seed_ranges.copy()
        
        for k, key in enumerate(mapping.keys()):
            print("Currently mapping : ", key)
            completed_all_segments = False
            segment_index = 0
            while completed_all_segments == False:
                print("\n")
                current_seed_range = seeds_mapped_to_location[segment_index]
                print("Currently analyzing seeds in range : ", current_seed_range)
                
                # go through the six cases of the seed range and the modified range
                for i in range(len(mapping[key])):
                    if (current_seed_range[0] >= mapping[key][i][1]) & (current_seed_range[0] < mapping[key][i][1] + mapping[key][i][2]):
                        # print("Left side is inside modified range")
                        seeds_mapped_to_location[segment_index][0] += mapping[key][i][0] - mapping[key][i][1]
                        if current_seed_range[1] <= mapping[key][i][1] + mapping[key][i][2]:
                            # print("Right side is inside modified range")
                            seeds_mapped_to_location[segment_index][1] += mapping[key][i][0] - mapping[key][i][1]
                            break
                        else:
                            # print("Right side is to the right of modified range")
                            leftover_range = [mapping[key][i][1] + mapping[key][i][2] + 1, current_seed_range[1]]
                            seeds_mapped_to_location.append(leftover_range) # add the leftover range to the end of the list
                            seeds_mapped_to_location[segment_index][1] = mapping[key][i][0] + mapping[key][i][2]
                            break
                    elif current_seed_range[0] < mapping[key][i][1]:
                        # print("Left side is to the left of modified range")
                        if (current_seed_range[1] <= mapping[key][i][1] + mapping[key][i][2]) & (current_seed_range[1] > mapping[key][i][1]):
                            # print("Right side is inside modified range")
                            leftover_range = [current_seed_range[0], mapping[key][i][1]]
                            seeds_mapped_to_location.append(leftover_range) # add the leftover range to the end of the list
                            seeds_mapped_to_location[segment_index][0] = mapping[key][i][0]
                            seeds_mapped_to_location[segment_index][1] += mapping[key][i][0] - mapping[key][i][1]
                            break
                        elif current_seed_range[1] > mapping[key][i][1] + mapping[key][i][2]:
                            # print("Right side is to the right of modified range")
                            leftover_range_0 = [current_seed_range[0], mapping[key][i][1]]
                            leftover_range_1 = [mapping[key][i][1] + mapping[key][i][2] + 1, current_seed_range[1]]
                            seeds_mapped_to_location.append(leftover_range_0)
                            seeds_mapped_to_location.append(leftover_range_1)
                            seeds_mapped_to_location[segment_index][0] = mapping[key][i][0]
                            seeds_mapped_to_location[segment_index][1] = mapping[key][i][0] + mapping[key][i][2]
                            break
                        else:
                            # print("Right side is to the left of modified range")
                            continue
                    else:
                        # print("Left side is to the right of modified range")
                        continue
    
                print("New range(s) : ", seeds_mapped_to_location[segment_index])
            
                if segment_index == len(seeds_mapped_to_location) - 1:
                    completed_all_segments = True
                segment_index += 1
                
        print("Seeds mapped to location : ", seeds_mapped_to_location)
        print("Minimum location : ", min(min(seeds_mapped_to_location)))
                        
        
            
        
        