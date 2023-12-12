plane = []
galaxies = []
with open('inputs/11.txt', 'r') as file:
    for line in file:
        plane.append(list(line.strip()))


rowCont = [0 for _ in range(len(plane))]
colCont = [0 for _ in range(len(plane[0]))]

for i in range(len(plane)):
    for j in range(len(plane[i])):
        if plane[i][j] == '#':
            galaxies.append((i, j))
            rowCont[i] += 1
            colCont[j] += 1


accumRow = [0 for _ in range(len(plane))]
accumCol = [0 for _ in range(len(plane[0]))]

expansionFactor = 1000000

for i in range(1, len(plane)):
    accumRow[i] = accumRow[i-1]
    if rowCont[i] == 0:
        accumRow[i] += expansionFactor - 1

for i in range(1, len(plane[0])):
    accumCol[i] = accumCol[i-1]
    if colCont[i] == 0:
        accumCol[i] += expansionFactor-1

# for galaxy in galaxies:
#     x, y = galaxy
#     print((x,y))
#     print(accumRow[x], accumCol[y])

total = 0
for i in range(len(galaxies)):
    x, y = galaxies[i]
    for j in range(i+1, len(galaxies)):
        nx, ny = galaxies[j]

        newX = x + accumRow[x]
        newNx = nx + accumRow[nx]
        newY = y + accumCol[y]
        newNy = ny + accumCol[ny]

        dist = abs(newX-newNx) + abs(newY-newNy)
        total += dist
        # print("dist from ", i, " to ", j, " is ", dist)

print(total)