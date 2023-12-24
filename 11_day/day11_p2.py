D = open("day11.txt").read().strip()
L = D.split("\n")
ans = 0

# get the vertices of the galaxies and the blank columns/rows
blank_rows = [x for x in range(len(L))]
blank_columns = [x for x in range(len(L[0]))]
vertices = []
for y, line in enumerate(L):
    for x, char in enumerate(line):
        if char == "#":
            vertices.append([x, y])
            if x in blank_columns:
                blank_columns.remove(x)
            if y in blank_rows:
                blank_rows.remove(y)

# each blank row counts as two
for vertice in vertices.copy():
    push_rows = 0
    for row in blank_rows:
        if vertice[1] > row:
            push_rows += 999999
    vertices.remove(vertice)
    vertices.append([vertice[0], vertice[1] + push_rows - 1])

# each blank column counts as two
for vertice in vertices.copy():
    push_columns = 0
    for column in blank_columns:
        if vertice[0] > column:
            push_columns += 999999
    vertices.remove(vertice)
    vertices.append([vertice[0] + push_columns - 1, vertice[1]])

# find shortest path
for i, start_vertice in enumerate(vertices):
    for end_vertice in vertices[i+1:]:
        add = abs(end_vertice[0] - start_vertice[0]) + abs(end_vertice[1] - start_vertice[1])
        ans += add
print(ans)