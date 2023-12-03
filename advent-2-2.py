file_path = "/mnt/home/tha10/advent-of-code-23/input-2-0.txt"
max_dict = {"red": 12, "green": 13, "blue": 14}

def strip_inputs(line): # supply the entire line as input
    [game_id, game_data] = line.split(":")
    number_id  = int(game_id.split("Game ")[1])
    draw_results = game_data.split("; ")
    largest_dict = {"red": 0, "green": 0, "blue": 0}

    for draw in draw_results:
        color_split = draw.strip().split(", ")
        # print(color_split)
        for color in color_split:
            num = color.split(" ")[0]
            c = color.split(" ")[1]
            if largest_dict[c] < int(num):
                largest_dict[c] = int(num)

    return [number_id, largest_dict["red"], largest_dict["green"], largest_dict["blue"]]

if __name__ == "__main__":
    with open(file_path, "r") as file:
        values_per_line = []
        sum_of_all_game_powers = 0

        for line in file:
            game = strip_inputs(line)
            print(strip_inputs(line))
            power_of_game = game[1] * game[2] * game[3]
            sum_of_all_game_powers += power_of_game


        print("Sum of all game ids = ", sum_of_all_game_powers)
