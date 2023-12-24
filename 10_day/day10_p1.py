D = open("day10.txt", "r").read().strip()
L = D.split("\n")
ans = 1

start = []
directions = {}
for row, line in enumerate(L):
    for index, char in enumerate(line):
        if char == "F":
            directions[f'{row} {index}'] = [[row+1, index], [row, index+1]]
        elif char == "7":
            directions[f'{row} {index}'] = [[row+1, index], [row, index-1]]
        elif char == "J":
            directions[f'{row} {index}'] = [[row-1, index], [row, index-1]]
        elif char == "L":
            directions[f'{row} {index}'] = [[row-1, index], [row, index+1]]
        elif char == "|":
            directions[f'{row} {index}'] = [[row+1, index], [row-1, index]]
        elif char == "-":
            directions[f'{row} {index}'] = [[row, index-1], [row, index+1]]
        elif char == "S":
            start = [row, index]
        else:
            directions[f'{row} {index}'] = [1, 1]

currentLocation = []
for _ in range(2):
    if (directions.get(f'{start[0]} {start[1]+1}', ['a'])[0] == start or directions.get(f'{start[0]} {start[1]+1}', ['a', 'b'])[1] == start) and (not f'{start[0]} {start[1]+1}' in currentLocation):
        currentLocation.append(f'{start[0]} {start[1]+1}')
    elif (directions.get(f'{start[0]} {start[1]-1}', ['a'])[0] == start or directions.get(f'{start[0]} {start[1]-1}', ['a', 'b'])[1] == start) and (not f'{start[0]} {start[1]-1}' in currentLocation):
       currentLocation.append(f'{start[0]} {start[1]-1}')
    elif (directions.get(f'{start[0]+1} {start[1]}', ['a'])[0] == start or directions.get(f'{start[0]+1} {start[1]}', ['a', 'b'])[1] == start) and (not f'{start[0]+1} {start[1]}' in currentLocation):
        currentLocation.append(f'{start[0]+1} {start[1]}')
    elif (directions.get(f'{start[0]-1} {start[1]}', ['a'])[0] == start or directions.get(f'{start[0]-1} {start[1]}', ['a', 'b'])[1] == start) and (not f'{start[0]-1} {start[1]}' in currentLocation):
        currentLocation.append(f'{start[0]-1} {start[1]}')

print(currentLocation)

finished = False
Lastlocation1 = " ".join(map(str, start))
NextLocation1 = currentLocation[0]
LastLocation2 = " ".join(map(str, start))
NextLocation2 = currentLocation[1]
print("last locations", Lastlocation1, LastLocation2, "Next Locations", NextLocation1, NextLocation2)
while not finished:
    #print([x for x in directions[NextLocation1] if not f'{x[0]} {x[1]}' == Lastlocation1], directions[NextLocation1], Lastlocation1)
    this_locaiton = NextLocation1
    NextLocation1 = " ".join(map(str, [x for x in directions[NextLocation1] if not f'{x[0]} {x[1]}' == Lastlocation1][0]))
    Lastlocation1 = this_locaiton
    print('next', NextLocation1, "|", Lastlocation1)


    #print([x for x in directions[NextLocation2] if f'{x[0]} {x[1]}' == LastLocation2], directions[NextLocation2], LastLocation2)
    this_locaiton = NextLocation2
    NextLocation2 = " ".join(map(str, [x for x in directions[NextLocation2] if not f'{x[0]} {x[1]}' == LastLocation2][0]))
    LastLocation2 = this_locaiton
    print('next', NextLocation2, "|", LastLocation2)


    print(NextLocation1, NextLocation2)
    
    ans+=1
    
    if NextLocation1 == NextLocation2:
        finished = True

print(ans)