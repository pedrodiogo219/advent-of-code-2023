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
            rowCont[i] += 1
            colCont[j] += 1

for i in range(len(colCont)-1, -1, -1):
    if colCont[i] == 0:
        for row in range(len(plane)):
            plane[row].insert(i, '.')

for i in range(len(rowCont)-1, -1, -1):
    if rowCont[i] == 0:
        plane.insert(i, ['.' for _ in range(len(plane[0]))])

# for i in range(len(plane)):
#     print("".join(plane[i]))

for i in range(len(plane)):
    for j in range(len(plane[i])):
        if plane[i][j] == '#':
            galaxies.append((i, j))

# print(galaxies)

total = 0
for i in range(len(galaxies)):
    x, y = galaxies[i]
    for j in range(i+1, len(galaxies)):
        nx, ny = galaxies[j]
        dist = abs(x-nx) + abs(y-ny)
        total += dist
        # print("dist from ", i, " to ", j, " is ", dist)

print(total)