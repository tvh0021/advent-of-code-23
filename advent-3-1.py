file_path = "/mnt/home/tha10/advent-of-code-23/input-3-0.txt"

def is_a_symbol(s):
    """Determine if a given character is a symbol.

    Args:
        s (str): The character to check

    Returns:
        bool: True if the character is a symbol, False otherwise
    """
    if s in {'-', '*', '/', '&', '+', '#', '%', '@', '$', '='}:
        return True
    else:
        return False

def scan_for_numbers(line):
    """Scan a line for numbers and return a list of them, plus the indices of the first and last characters of each number.

    Args:
        line (str): The line to scan

    Returns:
        list[list]: list of lists, each containing the number, the index of the first character of the number, and the index of the last character of the number
    """
    width = len(line)
    index_left = 0
    index_right = 0
    
    final_list = []
    
    # Scan from the left side of the line, jump to the right index when a number is found, and then continue scanning from there
    while index_left < width:
        # if a digit is found, extend the number to the right until a non-digit is found
        if line[index_left].isnumeric():
            
            current_number = int(line[index_left])
            this_left_index = index_left
            this_right_index = index_left
            
            for index_right in range(index_left + 1, width):
                if line[index_right].isnumeric() == True:
                    current_number = current_number * 10 + int(line[index_right])
                    this_right_index = index_right
                    # print(current_number, index_left, index_right)
                else:
                    index_left = index_right + 1
                    break
            
            final_list.append([current_number, this_left_index, this_right_index])
        else:
            index_left += 1
            
    return final_list

def is_symbol_in_neighborhood(text, line_index, left_index, right_index):
    """Check if a symbol is in the neighborhood of a number.

    Args:
        left_index (int): The index of the leftmost character of the number
        right_index (int): The index of the rightmost character of the number
        line_index (int): The line index of the number
        text (str): The text to search through

    Returns:
        bool: True if a symbol is found, False otherwise
    """
    height = len(text)
    width = len(text[0])

    for i in range(-1 if (line_index > 0) else 0, 2 if (line_index < height - 1) else 1):
        for j in range(left_index - 1 if (left_index > 0) else 0, right_index + 2 if (right_index < width - 1) else right_index + 1):
            if is_a_symbol(text[line_index + i][j]):
                return True

    return False

if __name__ == '__main__':

    file = open(file_path, "r") 
  
    # reading the file 
    data = file.read() 
    
    # replacing end splitting the text  
    # when newline ('\n') is seen. 
    file_as_list = data.split("\n") 
    # print(file_as_list)
    file.close() 

    unique_set = set()
    # a hack to make the last line of the file have a period at the end, circumventing the infinite loop problem
    for i in range(len(file_as_list)):
        file_as_list[i] += "."

    height = len(file_as_list)
    width = len(file_as_list[0])

    for i in range(height):
        for j in range(width):
            if (file_as_list[i][j] not in unique_set) and (file_as_list[i][j].isnumeric() == False) and (file_as_list[i][j] != '.'):
                unique_set.add(file_as_list[i][j])

    print("Set of unique symbols : ", unique_set)
    
    numbers_with_symbols = []
    
    for i in range(height):
        numbers_in_line = scan_for_numbers(file_as_list[i])
        print("Numbers in line ", i, " : ", numbers_in_line)
        numbers_with_symbols_in_line = []
        for number in numbers_in_line:
            if is_symbol_in_neighborhood(file_as_list, i, number[1], number[2]) == True:
                numbers_with_symbols_in_line.append(number[0])
        print("Numbers with adjacent symbol in line ", i, " : ", numbers_with_symbols_in_line)
        
        numbers_with_symbols.append(numbers_with_symbols_in_line)
    print("Numbers with adjacent symbol : ", numbers_with_symbols)
    total_sum =  sum([sum(numbers_with_symbols[i]) for i in range(height)])
    
    print("Total sum of numbers with adjacent symbols : ", total_sum)