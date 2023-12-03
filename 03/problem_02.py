
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

def is_gear(character): 
    return True if character == "*" else False

def is_character_part_character(character): 
    return False if character == "." or character.isdigit() or character == "\n" else True

def inside_bounds(index, line): 
    return False if line == None else True if index >= 0 and index < len(line) else False

def is_adjacent_to_gear(top_line, line, bottom_line, numbers, line_index): 

    # (relative y digit, absolute x index)
    g = []

    for number_indices in numbers: 

        gears_adjacents = []

        for index in number_indices:

            # Top
            if inside_bounds(index, top_line) and is_gear(top_line[index]): 
                gears_adjacents.append((- 1 + line_index, index, find_number(line, number_indices)))
                break
                
            # Bottom
            if inside_bounds(index, bottom_line) and is_gear(bottom_line[index]): 
                gears_adjacents.append((1 + line_index, index, find_number(line, number_indices)))
                break
            
            #  Bottom left
            if inside_bounds(index - 1, bottom_line) and is_gear(bottom_line[index - 1]): 
                gears_adjacents.append((1 + line_index, index -1, find_number(line, number_indices) ))
                break
            
            # Top left
            if inside_bounds(index - 1, top_line) and is_gear(top_line[index - 1]): 
                gears_adjacents.append((-1 + line_index, index - 1, find_number(line, number_indices)))
                break
            
            # Bottom right 
            if inside_bounds(index + 1, bottom_line) and is_gear(bottom_line[index + 1]): 
                gears_adjacents.append((1 + line_index, index + 1, find_number(line, number_indices)))
                break
            
            # Top right
            if inside_bounds(index + 1, top_line) and is_gear(top_line[index + 1]): 
                gears_adjacents.append((-1 + line_index, index + 1, find_number(line, number_indices)))
                break
            
            # Right
            if inside_bounds(index + 1, line) and is_gear(line[index + 1]): 
                gears_adjacents.append((0 + line_index, index + 1, find_number(line, number_indices)))
                break
            
            # Left
            if inside_bounds(index - 1, line) and is_gear(line[index - 1]): 
                gears_adjacents.append((0 + line_index, index - 1, find_number(line, number_indices)))
                break

        if not gears_adjacents == []:
            g.append(gears_adjacents)

    return g

def find_number(line, number_indices): 

    number_str = ""

    for index in number_indices: 
        number_str += line[index]

    return int(number_str)

if __name__ == "__main__": 
    data_file = open("03/data_01.txt")
    # data_file = open("03/data_test.txt")
    lines = data_file.readlines()
    data_file.close()

    all_gears_info = []
    for i, line in enumerate(lines):
        top_line = None if i == 0 else lines[i - 1]
        bottom_line = None if i == len(lines) - 1 else lines[i + 1]

        numbers_indices = find_all_number_in_line(line)
        gears_info = is_adjacent_to_gear(top_line, line, bottom_line, numbers_indices, i)
        all_gears_info += gears_info

    temp_all_gears = []
    for gear in all_gears_info:
        temp_all_gears.append(gear[0])

    all_gears_info = temp_all_gears

    # Check if two numbers are adjacent to the same gear
    # Then calculate the gear ratio

    total_sum = 0 
    for i in range(len(all_gears_info)): 
        for j in range(len(all_gears_info)): 
            if i == j: 
                continue

            if all_gears_info[i][0] == all_gears_info[j][0] and all_gears_info[i][1] == all_gears_info[j][1]:
                print(f"{all_gears_info[i][2]} * {all_gears_info[j][2]}")
                total_sum += ((all_gears_info[i][2] * all_gears_info[j][2]) / 2.0)

    total_sum = int(total_sum)

    print(total_sum)