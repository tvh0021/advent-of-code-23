import numpy as np

file_path = "/mnt/home/tha10/git_repos/advent-of-code-23/input-4-0.txt"

def number_of_matches(input, reference):
    """Determine if a given input matches a reference.

    Args:
        input (2d array): The input to check
        reference (2d array): The reference to check against

    Returns:
        1d array: The number of matches per card
    """
    number_of_matches = np.zeros(input.shape[0], dtype=int)

    for i, input_line in enumerate(input):
        reference_line = reference[i,:]
        number_of_matches[i] = np.sum(np.in1d(input_line, reference_line))
    
    return number_of_matches

def total_scratchcards(number_of_matches):
    """Determine the total number of copies of each scratchcard, following the rules from the problem statement.

    Args:
        number_of_matches (1d array): The number of matches per card

    Returns:
        1d array: The number of copies of each scratchcard
    """

    total = np.ones(number_of_matches.shape[0], dtype=int)

    for i in range(number_of_matches.shape[0]):
        total[i+1:i+1+number_of_matches[i]] += 1 * total[i]

    return total

if __name__ == "__main__":
    with open(file_path, "r") as f:
        input_file = f.read().split("\n")
    
    results = [i.split(": ")[1] for i in input_file]
    # print("Result of each scratch card : ", results)

    reference_array = np.array([i.split(" | ")[0].split() for i in results], dtype=int)
    input_array = np.array([i.split(" | ")[1].split() for i in results], dtype=int)
    
    # print("Reference array : ", reference_array[2,:])
    # print("Input array : ", input_array[2,:])

    # matches = np.in1d(input_array[40,:], reference_array[40,:])
    # print("Matches : ", np.sum(matches))

    match_tally_per_game = number_of_matches(input_array, reference_array)
    # print("Match tally per game : ", match_tally_per_game)

    points_per_game = np.zeros(len(match_tally_per_game), dtype=int)
    for i in range(len(match_tally_per_game)):
        if match_tally_per_game[i] == 0:
            points_per_game[i] = 0
        else:
            points_per_game[i] = 2**(match_tally_per_game[i]-1)

    print("Total points for part 1 : ", np.sum(points_per_game))

    total_scratchcards_per_game = total_scratchcards(match_tally_per_game)
    # print("Total scratchcards per game : ", total_scratchcards_per_game)

    print("Total number of scratchcards for part 2: ", np.sum(total_scratchcards_per_game))  