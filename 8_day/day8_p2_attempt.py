from math import lcm

D = open("day8.txt", "r").read().strip()
L = D.split("\n")
ans = 0
directions = L[0].strip()

def followDirections(ans, map, locations):
    for rl in directions:
        ans+=1
        zs = 0
        newLocations = []
        for location in locations:
            if rl == "R":
                if map[location][1][2] == "Z":
                    zs+=1
                newLocations.append(map[location][1])
            else:
                if map[location][0][2] == "Z":
                    zs+=1
                newLocations.append(map[location][0])
        if zs == len(locations):
            return True, newLocations, ans
        locations = newLocations
    return False, newLocations, ans

map = {}
for line in L[2:]:
    node, locations = line.split(" = ")
    left, right = locations[1: -1].split(", ")
    map[node] = (left, right)
startingLocations = []
for key in map.keys():
    if key[2] == "A":
        startingLocations.append(key)

end, currentLocations, ans = followDirections(ans, map, startingLocations)
while not end:
    end, currentLocations, ans = followDirections(ans, map, currentLocations)
print(ans)