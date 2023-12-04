def isDigit(c):
    return '0' <= c and c <= '9'


DX = [-1, 0, 1]
DY = [-1, 0, 1]

plane = []
with open('inputs/3.txt', 'r') as file:
    for line in file:
        line = str(line.strip())
        plane.append('.' + line + '.')

ROWS = len(plane)
COLS = len(plane[0])-2
# print(ROWS, COLS)

plane.insert(0, ['.' for _ in range(0, COLS + 2)])
plane.append(['.' for _ in range(0, COLS + 2)])

isValidNumber = [ [False for _ in range(0, COLS + 2)] for _ in range(0, ROWS + 2)] 

numbers = 0
ratios = 0
for i in range(1, ROWS+1):
    for j in range(1, COLS+1):
        # its a special charascter
        if plane[i][j] != "." and not isDigit(plane[i][j]):
            adjacentNumbers = []

            for dx in DX:
                for dy in DY:
                    if dx == 0 and dy == 0:
                        continue
                    neighborX = i + dx
                    neighborY = j + dy
                    
                    if not isValidNumber[neighborX][neighborY] and isDigit(plane[neighborX][neighborY]):
                        # print("X", neighborX)
                        # print("Y", neighborY)
                        isValidNumber[neighborX][neighborY] = True
                        init = neighborY
                        ending = neighborY
                        while isDigit(plane[neighborX][init-1]):
                            isValidNumber[neighborX][init-1] = True
                            init-=1
                        while isDigit(plane[neighborX][ending+1]):
                            isValidNumber[neighborX][ending+1] = True
                            ending+=1
                        # print(neighborX, init, ending)
                        currentNumber = int(plane[neighborX][init:ending+1])
                        numbers+=currentNumber
                        if plane[i][j] == '*':
                            adjacentNumbers.append(currentNumber)
            
            if len(adjacentNumbers) == 2:
                ratios += adjacentNumbers[0] * adjacentNumbers[1]


                        
print(numbers)     
print(ratios)                   
