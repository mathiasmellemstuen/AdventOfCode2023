words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def word_to_digit(line, index, forward = True): 
    for word_ind, word in enumerate(words): 
        if forward: 
            for i, word_character in enumerate(word): 
                if not word_character == line[index + i]:
                    break

                if i == len(word) - 1:
                    return word_ind + 1

            # for i in range(index, len(line)): 
            #         if i - index < 0 or i - index >= len(word): 
            #             break

            #         if not word[i - index] == line[i]:
            #             continue

            #         if i - index == len(word) - 1: 
            #             return word_ind + 1
        
        if not forward: 
            
            word = word[::-1]

            for i, word_character in enumerate(word):
                if not word_character == line[len(line) - index - i - 1]:
                    break

                if i == len(word) - 1:
                    return word_ind + 1
    return None
if __name__ == "__main__": 
    data_file = open("data_01.txt")
    lines = data_file.readlines()
    data_file.close()

    summed = 0

    for line in lines: 
        first_digit = None
        last_digit= None

        n = len(line)
        for i in range(n): 
            if line[i].isdigit() and first_digit == None:
                first_digit = int(line[i])

            if first_digit == None: 
                first_digit = word_to_digit(line, i, True)

            if line[n - i - 1].isdigit() and last_digit == None:
                last_digit = int(line[n - i - 1])
            
            if last_digit == None: 
                last_digit = word_to_digit(line, i, False)

            if last_digit != None and first_digit != None: 
                break
        
        current_digit = first_digit * 10 + last_digit
        print(current_digit)
        summed += current_digit 
    
    print(summed)
