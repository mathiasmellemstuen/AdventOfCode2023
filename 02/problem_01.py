wanted_red = 12
wanted_green = 13
wanted_blue = 14
wanted_total = wanted_red + wanted_green + wanted_blue


def format_line(line): 
    sets = line[line.find(":"):].split(";")

    game = []
    for current_set in sets:

        current_draw = {"blue": 0, "red": 0, "green": 0}
        for element in current_set.split(","):

            from_i = 1 + 1 if ":" in element else 0
            if " blue" in element:
                current_draw["blue"] = int(element[from_i:element.find(" blue")])

            if " red" in element:
                current_draw["red"] = int(element[from_i:element.find(" red")])
            
            if " green" in element:
                current_draw["green"] = int(element[from_i:element.find(" green")])

        game.append(current_draw)
    
    return game

def is_game_possible(game): 
    # remaining_total = wanted_total

    # amount_of_reds = sum([sub["red"] for sub in game])
    # amount_of_blues = sum([sub["blue"] for sub in game])
    # amount_of_greens = sum([sub["green"] for sub in game])

    values = []
    for t in game:
        total = t["red"] + t["blue"] + t["green"]

        values.append(t["red"] <= wanted_red and t["blue"] <= wanted_blue and t["green"] <= wanted_green and wanted_total >= total)
    
    return False not in values
    # remaining_total = amount_of_blues - amount_of_reds - amount_of_greens

    # return wanted_total >= amount_of_reds + amount_of_blues + amount_of_greens and amount_of_reds <= wanted_red and amount_of_blues <= wanted_blue and amount_of_greens <= wanted_green

if __name__ == "__main__": 
    data_file = open("02/data_01.txt")
    lines = data_file.readlines()
    data_file.close()

    result = 0
    for i, line in enumerate(lines): 
        game_id = i + 1
        game = format_line(line)

        result += game_id if is_game_possible(game) else 0
        print(is_game_possible(game))
    print(result)
