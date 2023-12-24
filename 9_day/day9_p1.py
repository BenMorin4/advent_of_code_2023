D = open("day9.txt", "r").read().strip()
L = D.split("\n")
ans = 0

def getLowerValues(values):
    newValues = []
    for index, _ in enumerate(values[:-1]):
        newValues.append(int(values[index + 1] - values[index]))
    return newValues

for line in L:
    values = [int(x) for x in line.split()]
    allZeroes = all(x == 0 for x in values)
    allValues = [values]
    while not allZeroes:
        lowerValues = getLowerValues(values)
        allValues.append(lowerValues)
        values = lowerValues
        allZeroes = all(x == 0 for x in values)

    lastValues = [val[-1] for val in allValues]
    prevCreatedVal = 0
    for i, val in enumerate(lastValues[1:]):
        prevCreatedVal = prevCreatedVal + lastValues[i]
    ans += prevCreatedVal
print(ans)