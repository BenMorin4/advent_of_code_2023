from math import lcm

D = open("day8.txt", "r").read().strip()
L = D.split("\n")
ans = 0
directions = L[0].strip()

def followDirections(step, map, location):
    for rl in directions:
        step+=1
        if rl == "R":
            newLocation = map[location][1]
        else:
            newLocation = map[location][0]
        if newLocation == "ZZZ":
            return "ZZZ", step
        location = newLocation
    return location, step

map = {}
for line in L[2:]:
    node, locations = line.split(" = ")
    left, right = locations[1: -1].split(", ")
    map[node] = (left, right)
startingLocations = []
for key in map.keys():
    if key[2] == "A":
        startingLocations.append(key)

totalSteps = []
for startLocation in startingLocations:
    step = 0
    location, step = followDirections(step, map, startLocation)
    while not location.endswith("Z"):
        location, step = followDirections(step, map, location)
    totalSteps.append(step)
print(lcm(*totalSteps))