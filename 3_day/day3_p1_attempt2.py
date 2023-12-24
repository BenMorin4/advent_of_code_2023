

intOrDot = "0 1 2 3 4 5 6 7 8 9 0 .".split(" ")
numsLocations = {}
symbolsLocaitons = []

def main():
    with open("./day3.txt", "r") as file:
        lines = file.readlines()
        for y, line in enumerate(lines):
            num = False
            line = line.strip()

            for index, char in enumerate(line):
                if index == len(line) - 1 and not num == False:
                    if char.isnumeric():
                        num = str(num) + str(char)
                    if not char in intOrDot:
                        symbolsLocaitons.append([index, y])

                    surroundingLocaitons = getSurroundingLocations(index - 1, y, len(num))
                    if num in numsLocations:
                        numsLocations[num].append(surroundingLocaitons)
                    else:
                        numsLocations[num] = [surroundingLocaitons]
                    num = False

                    if num in numsLocations:
                        numsLocations[num].append(surroundingLocaitons)
                    else:
                        numsLocations[num] = [surroundingLocaitons]
                    num = False

                elif char.isnumeric():
                    if num:
                        num = str(num) + str(char)
                    else:
                        num = str(char)

                elif not char in intOrDot:
                    if num:
                        surroundingLocaitons = getSurroundingLocations(index - 1, y, len(num))
                        if num in numsLocations:
                            numsLocations[num].append(surroundingLocaitons)
                        else:
                            numsLocations[num] = [surroundingLocaitons]

                    symbolsLocaitons.append([index, y])
                    num = False
                else:
                    if num:
                        surroundingLocaitons = getSurroundingLocations(index - 1, y, len(num))
                        if num in numsLocations:
                            numsLocations[num].append(surroundingLocaitons)
                        else:
                            numsLocations[num] = [surroundingLocaitons]
                    num = False

        ans = 0
        for num, locationsList in numsLocations.items(): 
            found = False
            for locations in locationsList:
                found = False
                for location in locations:                   
                    if found:
                        continue
                    if location in symbolsLocaitons:
                        ans += int(num)
                        found = True
                        continue
        print(ans)

    # missing a few numbers

def getSurroundingLocations(index, line, length):
    possibleLocations = []
    for charNum in range(length):
        for y in [-1, 0, 1]:
            for x in [-1, 0, 1]:
                if not [int(index) + x - charNum, int(line) + y] in possibleLocations:
                    possibleLocations.append([int(index) + x - charNum, int(line) + y])
    return possibleLocations

if __name__ == "__main__":
    main()
