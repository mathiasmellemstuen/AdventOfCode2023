n_processed = 0

def winnings_length(card): 
   return len(list(set(card["winning"]).intersection(card["current"])))

def recursively_process_card(i, cards):
    global n_processed
    n_processed += 1
    n_wins = winnings_length(cards[i])

    for j in range(n_wins): 
        recursively_process_card(i + j + 1, cards)

if __name__ == "__main__": 
    data_file = open("04/data_01.txt")
    lines = data_file.readlines()
    data_file.close()

    cards = []
    for line in lines:
        current_line = line.strip('\n').split(":")[1]
        items = [current_line.split("|")[0].split(" "), current_line.split("|")[1].split(" ")]
        items[0] = [int(x) for x in items[0] if x != ""]
        items[1] = [int(x) for x in items[1] if x != ""]
        cards.append({"winning": items[0], "current": items[1]})

    for i in range(len(cards)): 
        recursively_process_card(i, cards)

    print(n_processed)