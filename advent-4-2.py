file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-4-0.txt"

def number_of_matches(input, reference):
    """Determine if a given input matches a reference.

    Args:
        input (list): The input to check
        reference (list): The reference to check against

    Returns:
        int: The number of matches
    """
    number_of_matches = 0
    for i in input:
        if any(i == j for j in reference):
            number_of_matches += 1
    
    return number_of_matches

# def recursive_add(list_of_instances):
#     for i in range(len(list_of_instances)):
#         list_of_instances[i:] += recursive_add(list_of_instances[i+1:])
    
#     return list_of_instances

if __name__ == "__main__":
    file = open(file_path, "r") 
  
    # reading the file 
    data = file.read() 
    
    # replacing end splitting the text  
    # when newline ('\n') is seen. 
    file_as_list = data.split("\n") 
    # print(file_as_list)
    file.close() 

    results = [i.split(": ")[1] for i in file_as_list]

    # print(results)

    reference_list = []
    input_list = []
    for i in range(len(results)):
        input_list.append(results[i].split(" | ")[1].split())
        reference_list.append(results[i].split(" | ")[0].split())

    match_tally_per_game = [number_of_matches(input_list[i], reference_list[i]) for i in range(len(input_list))]
    print("Match tally per game : ", match_tally_per_game)
    print("Length of match tally per game : ", len(match_tally_per_game))
    
    cycle_reproduce = []
    for i in range(len(match_tally_per_game)):
        zeros = [0] * len(match_tally_per_game)
        if (i+1+match_tally_per_game[i]) > len(match_tally_per_game):
            end_range = len(match_tally_per_game)
        else:
            end_range = i+1+match_tally_per_game[i]
        for j in range(i+1, end_range):
            zeros[j] += 1
        cycle_reproduce.append(zeros)
    
    base_cy = [1] * len(match_tally_per_game) # every game starts with 1 copy of itself
    total = base_cy
    # print(len(cycle_reproduce))

    game = 0
    while game < len(cycle_reproduce):
        # print("Matches this game : ", cycle_reproduce[game])
        # print("Current total : ", total)
        total_before = total.copy()
        for index in range(1, len(cycle_reproduce)):
            # print("Index : ", index)
            # print("Current value : ", total_before[index])
            # print("Added value : ", total_before[index-1] * cycle_reproduce[game][index])
            total[index] = total_before[index-1] * cycle_reproduce[game][index] + total_before[index]
            # print("New value : ", total[index])
        
        game += 1

    print(total)
    print("Total number of games : ", len(total))
    print("Total number of scratchcards : ", sum(total))
        

  