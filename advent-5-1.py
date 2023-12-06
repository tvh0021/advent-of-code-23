
if __name__ == "__main__":
    with open("input-5-tst.txt") as f:
        seeds = f.readline().strip("seeds: ").strip("\n").split()
        seeds = [int(i) for i in seeds]
        
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
        
        print("Seeds : ", seeds)
        print("\n")
        print("Keys : ", mapping.keys())
        print("\n")
        print("Mapping : ", mapping)
        
        
        # now iterate through the seeds and find if the seed falls within the range of any of the maps, otherwise map it one-to-one
        seeds_mapped_to_location = seeds.copy()
        for s, seed in enumerate(seeds):
            print("\n")
            print("Currently analyzing seed : ", seed)
            for k, key in enumerate(mapping.keys()):
                print("Currently mapping : ", key)
                print("Original number : ", seeds_mapped_to_location[s])
                for i in range(len(mapping[key])):
                    if (seeds_mapped_to_location[s] >= mapping[key][i][1]) & (seeds_mapped_to_location[s] < mapping[key][i][1] + mapping[key][i][2]):
                        seeds_mapped_to_location[s] += mapping[key][i][0] - mapping[key][i][1]
                        break
                print("New number : ", seeds_mapped_to_location[s])
                
        print("Seeds mapped to location : ", seeds_mapped_to_location)
        print("Minimum location : ", min(seeds_mapped_to_location))