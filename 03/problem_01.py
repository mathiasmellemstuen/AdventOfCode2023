
def find_all_number_in_line(line):
    numbers = []

    for i, character in enumerate(line):
        if character.isdigit(): 
            if(len(numbers) == 0):
                numbers.append([i])
                continue

            if numbers[len(numbers) - 1] == []: 
                numbers[len(numbers) - 1].append(i)
                continue

            numbers[len(numbers) - 1].append(i)
        else: 
            if(len(numbers) == 0):
                numbers.append([])
                continue

            if numbers[len(numbers) - 1] != []:
                numbers.append([])

    # Removing empty lists that might occur
    for l in numbers: 
        if l == []: 
            numbers.remove(l)

    return numbers

def is_character_part_character(character): 
    return False if character == "." or character.isdigit() or character == "\n" else True

def inside_bounds(index, line): 
    return False if line == None else True if index >= 0 and index < len(line) else False

def is_valid_part(top_line, line, bottom_line, numbers): 

    valid = []

    for number_indices in numbers: 

        c_valid = False

        for index in number_indices:
            if inside_bounds(index, top_line) and is_character_part_character(top_line[index]): 
                c_valid = True
                break
            
            if inside_bounds(index, bottom_line) and is_character_part_character(bottom_line[index]): 
                c_valid = True
                break
            
            if inside_bounds(index - 1, bottom_line) and is_character_part_character(bottom_line[index - 1]): 
                c_valid = True
                break
            
            if inside_bounds(index - 1, top_line) and is_character_part_character(top_line[index - 1]): 
                c_valid = True
                break

            if inside_bounds(index + 1, bottom_line) and is_character_part_character(bottom_line[index + 1]): 
                c_valid = True
                break
            
            if inside_bounds(index + 1, top_line) and is_character_part_character(top_line[index + 1]): 
                c_valid = True
                break
            
            if inside_bounds(index + 1, line) and is_character_part_character(line[index + 1]): 
                c_valid = True
                break
            
            if inside_bounds(index - 1, line) and is_character_part_character(line[index - 1]): 
                c_valid = True
                break

        valid.append(c_valid)

    return valid

def find_number(line, number_indices): 

    number_str = ""

    for index in number_indices: 
        number_str += line[index]

    return int(number_str)

if __name__ == "__main__": 
    data_file = open("03/data_01.txt")
    lines = data_file.readlines()
    data_file.close()

    # line_length = len(lines[0])

    total_sum = 0

    for i, line in enumerate(lines):
        top_line = None if i == 0 else lines[i - 1]
        bottom_line = None if i == len(lines) - 1 else lines[i + 1]

        numbers_indices = find_all_number_in_line(line)
        numbers_validity = is_valid_part(top_line, line, bottom_line, numbers_indices)

        for j, valid in enumerate(numbers_validity): 
            if valid: 
                number = find_number(line, numbers_indices[j])
                total_sum += number
    
    print(total_sum)