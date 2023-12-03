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

def game_power(game): 
    all_reds = [sub["red"] for sub in game]
    all_blues = [sub["blue"] for sub in game]
    all_greens = [sub["green"] for sub in game]

    max_red = max(all_reds)
    max_blue = max(all_blues)
    max_green = max(all_greens)

    return max_red * max_blue * max_green

if __name__ == "__main__": 
    data_file = open("02/data_01.txt")
    lines = data_file.readlines()
    data_file.close()

    result = 0
    for i, line in enumerate(lines): 
        game_id = i + 1
        game = format_line(line)

        result += game_power(game) 
    print(result)
