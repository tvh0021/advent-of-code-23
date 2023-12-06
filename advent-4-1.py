file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-4-0.txt"

def matches(input, reference):
    """Determine if a given input matches a reference.

    Args:
        input (list): The input to check
        reference (list): The reference to check against

    Returns:
        int: The points to award based on the number of matches
    """
    number_of_matches = 0
    for i in input:
        if any(i == j for j in reference):
            number_of_matches += 1
    
    if number_of_matches == 0:
        return 0
    
    return int(2**(number_of_matches-1))

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

    # point_tally_per_game = []
    # for i in range(len(input_list)):
    #     point_tally_per_game.append(matches(input_list[i], reference_list[i]))
    point_tally_per_game = [matches(input_list[i], reference_list[i]) for i in range(len(input_list))]

    # print("Points tally per game", point_tally_per_game)
    print("Total points", sum(point_tally_per_game))