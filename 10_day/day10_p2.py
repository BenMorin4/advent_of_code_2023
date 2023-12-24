D = open("day10.txt", "r").read().strip()
L = D.split("\n")
ans = 0

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

#print(currentLocation, start)

# find the shape that the s character has
s_shape = "S"
location_difference = []
location_difference.append([int(currentLocation[0].split()[0]) - int(start[0]), int(currentLocation[0].split()[1]) - start[1]])
location_difference.append([int(currentLocation[1].split()[0]) - int(start[0]), int(currentLocation[1].split()[1]) - start[1]])
if [0, -1] in location_difference and [0, -1] in location_difference:
    s_shape = "-"
elif [1, 0] in location_difference and [-1, 0] in location_difference:
    s_shape = "|"
elif [1, 0] in location_difference and [0, 1] in location_difference:
    s_shape = "J"
elif [0, -1] in location_difference and [1, 0] in location_difference:
    s_shape = "7"
elif [-1, 0] in location_difference and [0, -1] in location_difference:
    s_shape = "F"
elif [-1, 0] in location_difference and [0, 1] in location_difference:
    s_shape = "L"

string_list = list(L[start[0]])
string_list[start[1]] = s_shape
L[start[0]] = ''.join(string_list)


loop_edges = [[str(start[0]), str(start[1])]]

finished = False
Lastlocation1 = " ".join(map(str, start))
NextLocation1 = currentLocation[0]
LastLocation2 = " ".join(map(str, start))
NextLocation2 = currentLocation[1]
while not finished:
    loop_edges.append([NextLocation1.split()[0], NextLocation1.split()[1]])
    loop_edges.append([NextLocation2.split()[0], NextLocation2.split()[1]])

    this_locaiton = NextLocation1
    NextLocation1 = " ".join(map(str, [x for x in directions[NextLocation1] if not f'{x[0]} {x[1]}' == Lastlocation1][0]))
    Lastlocation1 = this_locaiton

    this_locaiton = NextLocation2
    NextLocation2 = " ".join(map(str, [x for x in directions[NextLocation2] if not f'{x[0]} {x[1]}' == LastLocation2][0]))
    LastLocation2 = this_locaiton
    
    if NextLocation1 == NextLocation2:
        loop_edges.append([NextLocation1.split()[0], NextLocation1.split()[1]])
        finished = True

#print(loop_edges)

# loop though rows and cols
# for each row, perform ray casting algorithm to determine what dots are inside

for y, line in enumerate(L):
    inside = False
    direction = None
    for x, char in enumerate (line):
        if [str(y), str(x)] in loop_edges:
            if char == 'F':
                direction = 'down'
            elif char == 'L':
                direction = 'up'                
            elif char == '|' or char == 'J' or char == '7':
                if direction == 'up' and char == 'J':
                    direction = None
                elif direction == 'down' and char == '7':
                    direction = None
                elif not char == '|':
                    if inside == True:
                        inside = False
                    else:
                        inside = True
                elif inside == True:
                   inside = False
                else:
                   inside = True
                direction = None
        elif inside == True and direction == None:
            #print(y, x)
            ans += 1
    #print('line', line)

print(ans)