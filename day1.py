def main():
    lines = open("day1.txt", "r")
    total = 0
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    keys = []
    for key in words:
        keys.append(key)

    for line in lines:
        possibleWords = []
        index = 0
        for char in line:
            if char.isnumeric():
                x = char
                break

            if not possibleWords == []:
                for word in possibleWords:


            for key in keys:
                if char == key[0]:
                    # this needs to be key value to figure out where we are for each word
                    possibleWords.append(key)
                
            if possibleWords == []:
                index = 0
            else:
                index += 1

            continue
   
        for char in line [::-1]:
            if char.isnumeric():
                y = char
                break

        total += int(str(x) + str(y))
    print(total)      

if __name__ == "__main__":
    main()