import multiprocessing as mp
import time


def main():
    start = time.time()
    with open("day5.txt", "r") as file:
        lines = file.readlines()

        # Get seeds
        pairs = []
        seedsStrings = lines[0].strip().split(" ")
        seeds = [int(seed) for seed in seedsStrings[1:]]
        for index, seed in enumerate(seeds[::2]):
            pairs.append([int(seeds[index - 1]), int(seeds[index])])
        
        # print(pairs)
        finalLocations = []
        for pair in pairs:
            # execute the function for each num,

            # turn this into workers
            for num in range(pair[0], pair[0] + pair[1] - 1):
                finalLocation = mp.Process(target=GetFinalLocation, args=(num, lines))

                finalLocation = GetFinalLocation(num, lines)
                finalLocations.append(finalLocation)

        #print('stf', finalLocations)

        # Find lowest final location
        lowestLocation = False
        #print('stf[1]:', finalLocations)
        for location in finalLocations:
            
            if lowestLocation:
                if location < lowestLocation: lowestLocation = location
            else:
                lowestLocation = location
          
        end = time.time()
        print(end-start)
        print('final', lowestLocation)

def GetFinalLocation(seed, lines):
    # For each map
    isMap = False
    mapNum = 0
    mapn = 1
    currentLocation = seed
    for line in lines[2:]:
        line = line.strip()

        # If this is the map header
        if not line.find(":") == -1:
            #print('map', mapn, currentLocation)
            mapn += 1
            isMap = True
            found = False
            continue
        # This is a map node
        elif isMap == True:
            if found:
                continue
            # false map node, next line
            if (len(line) == 0):
                isMap = False
                #print("End Map")
                continue

            # Check our value against this line's range
            #print(line)
            currentLocation, newLocaiton = CheckLine(line, currentLocation)
            if newLocaiton:
                found = True
                continue

            # Add this to our map

        # 2nd or more blank line
        else:
            continue


    return currentLocation
    #print('Seed final location', currentLocation)

def CheckLine(line, location):
    numbersStrings = line.split(" ")
    numbers = [int(number) for number in numbersStrings]
    inputRange = [numbers[1], int(numbers[1] + numbers[2] - 1)]
    #print(location, inputRange)

    # If we are in this range, make the transformation, or dont if not
    if location >= inputRange[0] and location <= inputRange[1] :
        destination = location + (numbers[0] - numbers[1])
        #print('start', location, 'end', destination)
        return destination, True
    else:
        #print('no change', location)
        return location, False

if __name__ == "__main__":
    main()
