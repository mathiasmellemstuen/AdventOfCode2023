
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
            
            if line[n - i - 1].isdigit() and last_digit == None: 
                last_digit = int(line[n - i - 1])
            
            if last_digit != None and first_digit != None: 
                break
    
        summed += first_digit * 10 + last_digit
    
    print(summed)
