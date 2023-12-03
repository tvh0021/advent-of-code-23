if __name__ == "__main__":
    file_path = "/mnt/home/tha10/advent-of-code-23/input-1-0.txt"
    
    digit_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six" : 6, "seven": 7, "eight": 8, "nine": 9}
    begin_set = set([k[0] for k in digit_dict])
    end_set = set([k[-1] for k in digit_dict])

    with open(file_path, "r") as file:
        values_per_line = []
        for line in file:
            input = line.strip()
            value_out = 0

            # left pointer, starts from the beginning, go forward
            for n, i in enumerate(input):
                break_flag = False
                if i.isnumeric():
                    value_out += 10 * int(i)
                    break
                elif i in begin_set:
                    for m in digit_dict:
                        if input[n:n+len(m)] == m:
                            value_out += 10 * digit_dict[m]
                            break_flag = True
                            break
                    if break_flag:
                        break
                    
            # right pointer, starts from the end, go backward
            for n, j in enumerate(input[::-1]):
                break_flag = False
                if j.isnumeric():
                    value_out += int(j)
                    break
                elif j in end_set:
                    for m in digit_dict:
                        if input[len(input)-n-len(m):len(input)-n] == m:
                            value_out += digit_dict[m]
                            break_flag = True
                            break
                    if break_flag:
                        break
                    
            print(f"Number from string {input} : {value_out}")
            values_per_line.append(value_out)

    print("Sum of all numbers : ", sum(values_per_line))