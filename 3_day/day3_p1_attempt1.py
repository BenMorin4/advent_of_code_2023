
def main():
    ans = 0
    lineLength = False
    with open("day3_sp.txt", "r") as file:
        lines = file.readlines()
        for y, line in enumerate(lines):
            if not lineLength:
                lineLength = len(line)
            num = False
            for index, char in enumerate(line):
                # if it is a number we must add it to the num list
                if char.isnumeric():
                    # print(char, num)
                    if num:
                        num = str(num) + str(char)
                    else:
                        num = str(char)
                else:
                    # number has ended, is it a part number
                    if num:
                        isPartNumber = IsPartNumber(lines, index - 1, y, len(num), lineLength)
                        if isPartNumber:
                            print(num)
                            ans += int(num)
                            num = False
                            continue

                        num = False
                    else:           
                        num = False

        print(ans)

# check if number touches a symbol
def IsPartNumber(lines, endIndex, rowNum, numLength, lineLength):
    intOrDot = "0 1 2 3 4 5 6 7 8 9 0 .".split(" ")
    # check around this character to look for a symbol
    for index in range(numLength):
        print(lines[rowNum][endIndex-index])
        # check middle
        if not (lines[rowNum-1][endIndex-index] or lines[rowNum+1][endIndex-index]) in intOrDot:
            #print(lines[rowNum][endIndex-index])
            return True
        # check right side
        if endIndex - index + 1 == lineLength:
            continue
        elif not (lines[rowNum-1][endIndex-index+1] or lines[rowNum][endIndex-index+1] or lines[rowNum+1][endIndex-index+1]) in intOrDot:
            print(lines[rowNum][endIndex-index], lines[rowNum-1][endIndex-index+1], lines[rowNum][endIndex-index+1], lines[rowNum+1][endIndex-index+1])
            #print(lines[rowNum][endIndex-index])
            return True
        else:
            print(lines[rowNum][endIndex-index], lines[rowNum-1][endIndex-index+1], lines[rowNum][endIndex-index+1], lines[rowNum+1][endIndex-index+1])
        # check left side
        if endIndex - index == 0:
            continue
        elif not (lines[rowNum-1][endIndex-index] or lines[rowNum+-1][endIndex-index] or lines[rowNum-1][endIndex-index+1]) in intOrDot:
            #print(lines[rowNum][endIndex-index])
            return True
    return False
        
if __name__ == "__main__":
    main()