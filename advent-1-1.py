if __name__ == "__main__":
    file_path = "/mnt/home/tha10/advent-of-code-23/input-1-0.txt"


    with open(file_path, "r") as file:
        values_per_line = []
        for line in file:
            input = line.strip()
            pointer_left, pointer_right = 0, len(input) - 1
            value_out = 0

            for i in input:
                if i.isnumeric():
                    value_out += 10 * int(i)
                    break
                    
            for j in input[::-1]:
                if j.isnumeric():
                    value_out += int(j)
                    break
                    
            print("Number from string : ", value_out)
            values_per_line.append(value_out)

    print("Sum of all numbers : ", sum(values_per_line))