if __name__ == "__main__": 
    data_file = open("04/data_01.txt")
    lines = data_file.readlines()
    data_file.close()

    formatted_lines = []
    for line in lines:
        current_line = line.strip('\n').split(":")[1]
        items = [current_line.split("|")[0].split(" "), current_line.split("|")[1].split(" ")]
        items[0] = [int(x) for x in items[0] if x != ""]
        items[1] = [int(x) for x in items[1] if x != ""]
        formatted_lines.append({"winning": items[0], "current": items[1]})

    summed = 0

    for card in formatted_lines:
        winning = set(card["winning"])
        current = card["current"]
        
        number_of_equals = len(list(winning.intersection(current)))

        if number_of_equals != 0: 
            summed += 2 ** (number_of_equals - 1)
    
    print(summed)