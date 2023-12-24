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

                elif char.isnumeric():
                    if num:
                        num = str(num) + str(char)
                    else:
                        num = str(char)

                elif char == "*":
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

        starLocations = {}
        for num, locationsList in numsLocations.items():
            found = False
            for locations in locationsList:
                found = False
                for location in locations:
                    if found:
                        continue
                    if location in symbolsLocaitons:
                        locationWithSpace = str(location[0]) + ' ' + str(location[1])
                        if locationWithSpace in starLocations.keys():
                            starLocations[locationWithSpace].append(num)
                        else:
                            starLocations[locationWithSpace] = [num]
                        found = True
                        continue
        
        ans = 0
        for star, nums in starLocations.items():
            if len(nums) == 2:
                ans += int(nums[0]) * int(nums[1])


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
