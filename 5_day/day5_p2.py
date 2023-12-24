import multiprocessing as mp
import time
import threading
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')
app.conf.broker_url = 'redis://localhost:6379/0'

finalLocation1 = []
finalLocation2 = []

def gotoFinalLocation1(finalLocation): finalLocation1 = finalLocation
def gotoFinalLocation2(finalLocation): finalLocation2 = finalLocation


def main():
    start = time.time()
    with open("day5_short.txt", "r") as file:
        lines = file.readlines()

        # Get seeds
        pairs = []
        seedsStrings = lines[0].strip().split(" ")
        seeds = [int(seed) for seed in seedsStrings[1:]]
        for index, seed in enumerate(seeds[::2]):
            pairs.append([int(seeds[index - 1]), int(seeds[index])])
        
        # print(pairs)
        finalLocations = []

        worker1 = mp.Process(target=ExecuteFullRange, args=(pairs[0], lines, gotoFinalLocation1))
        worker2 = mp.Process(target=ExecuteFullRange, args=(pairs[1], lines, gotoFinalLocation2))

        worker1.start()
        worker2.start()

        print(finalLocation1, finalLocation2, min(finalLocation1, finalLocation2))

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

def ExecuteFullRange(pair, lines, finalLocation):
    storedLocation = float('inf')
    for num in range(pair[0], pair[0] + pair[1] - 1):
        thisLocation = GetFinalLocation(num, lines)
        if thisLocation < storedLocation: 
            storedLocation = thisLocation
    print('range executed', storedLocation)
    finalLocation(storedLocation)
    return

@app.task
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
