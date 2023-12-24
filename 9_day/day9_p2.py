D = open("day9.txt", "r").read().strip()
L = D.split("\n")
ans = 0

def getLowerValues(values):
    newValues = []
    for index, _ in enumerate(values[:-1]):
        newValues.append(int(values[index + 1] - values[index]))
    return newValues

for line in L:
    print('')
    values = [int(x) for x in line.split()]
    allZeroes = all(x == 0 for x in values)
    allValues = [values]
    while not allZeroes:
        lowerValues = getLowerValues(values)
        allValues.append(lowerValues)
        values = lowerValues
        allZeroes = all(x == 0 for x in values)

    firstValues = [val[0] for val in allValues[::-1]]
    prevCreatedVal = 0
    print(firstValues)
    for i, val in enumerate(firstValues):
        prevCreatedVal = firstValues[i] - prevCreatedVal
        print('prev val', prevCreatedVal)
    print('annss', prevCreatedVal)
    ans += prevCreatedVal
print(ans)