IMPOSSIBLE = (-1, -1, -1)
plane = []
memo = []

INF = 9999999

class Direction():
    def __init__(self, s):
        self.up = False
        self.right = False
        self.down = False
        self.left = False

        if s == "up":
            self.up = True
        if s == "right":
            self.right = True
        if s == "down":
            self.down = True
        if s == "left":
            self.left = True
    
    def __str__(self):
        return "up: %s, right: %s, down: %s, left: %s" % (self.up, self.right, self.down, self.left)


def findInit():
    ans = IMPOSSIBLE
    for i in range(0, ROWS+2):
        memo.append([])
        for j in range(0, COLS+2):
            memo[i].append(-INF)
            if plane[i][j] == 'S':
                ans = (i, j)

    return ans
            

def up(x, y):
    return x-1, y, Direction("down")

def right(x, y):
    return x, y+1, Direction("left")

def down(x, y):
    return x+1, y, Direction("up")

def left(x, y):
    return x, y-1, Direction("right")

def findNext(myChar, x, y, cameFrom):
    if myChar == '|':
        if cameFrom.up:
            return down(x, y)
        if cameFrom.down:
            return up(x, y)
        return IMPOSSIBLE
    
    if myChar == '-':
        if cameFrom.left:
            return right(x, y)
        if cameFrom.right:
            return left(x, y)
        return IMPOSSIBLE
    
    if myChar == 'L':
        if cameFrom.up:
            return right(x, y)
        if cameFrom.right:
            return up(x, y)
        return IMPOSSIBLE

    if myChar == 'J':
        if cameFrom.up:
            return left(x, y)
        if cameFrom.left:
            return up(x, y)
        return IMPOSSIBLE
    
    if myChar == '7':
        if cameFrom.left:
            return down(x, y)
        if cameFrom.down:
            return left(x, y)
        return IMPOSSIBLE
    
    if myChar == 'F':
        if cameFrom.right:
            return down(x, y)
        if cameFrom.down:
            return right(x, y)
        return IMPOSSIBLE
    
    if myChar == '.':
        return IMPOSSIBLE
    
    return IMPOSSIBLE


stack = []
def dfsStack():
    while len(stack):
        x, y, cameFrom, steps = stack.pop()

        print("I am: ", x, y, cameFrom, steps)
        if memo[x][y] != -INF:
            continue

        if plane[x][y] == 'S':
            memo[x][y] = 0
            continue
        
        nX, nY, nCameFrom = findNext(plane[x][y], x, y, cameFrom)
        print("I am going to: ", nX, nY, nCameFrom)

        if (nX, nY, nCameFrom) == IMPOSSIBLE:
            memo[x][y] = -INF
            continue
        
        if memo[nX][nY] != -INF:
            memo[x][y] = min(steps, memo[nX][nY]+1)
            if (x, y) == (2, 3):
                print(memo[x][y])
            continue
    
        stack.append((x, y, cameFrom, steps))
        stack.append((nX, nY, nCameFrom, steps+1))

def dfs(x, y, cameFrom, steps):
    if plane[x][y] == 'S':
        memo[x][y] = 0
        return 0

    nX, nY, nCameFrom = findNext(plane[x][y], x, y, cameFrom)

    stepsAfter = -INF
    if (nX, nY, nCameFrom) != IMPOSSIBLE:
        stepsAfter = dfs(nX, nY, nCameFrom, steps+1) + 1
    
    memo[x][y] = min(steps, stepsAfter)
    return memo[x][y]


with open('inputs/10.txt', 'r') as file:
    for line in file:
        line = str(line.strip())
        plane.append('.' + line + '.')

ROWS = len(plane)
COLS = len(plane[0])-2
# print(ROWS, COLS)

plane.insert(0, "".join(['.' for _ in range(0, COLS + 2)]))
plane.append("".join(['.' for _ in range(0, COLS + 2)]))

x, y = findInit()
memo[x][y] = 0

nX, nY, direc = up(x, y)
stack.append((nX, nY, direc, 1))
nX, nY, direc = right(x, y)
stack.append((nX, nY, direc, 1))
nX, nY, direc = down(x, y)
stack.append((nX, nY, direc, 1))
nX, nY, direc = left(x, y)
stack.append((nX, nY, direc, 1))

dfsStack()

ans = -INF
for i in range(0, ROWS+2):
    for j in range(0, COLS+2):
        ans = max(ans, memo[i][j])
        # print(i, j)
        # c = memo[i][j]
        # if c == -INF:
        #     c = '.'
        #     print("  .", end="")
        # else:
        #     print(" %02d" % (c,), end="")
    # print()

print(ans)

total = 0
for i in range(1, ROWS+1):
    colisions = 0
    for j in range(1, COLS+1):
        #empty space
        if memo[i][j] == -INF:
            if colisions % 2 == 1:
                total+=1
                # print((i, j), "is inside")
        else:
            if plane[i][j] in {'L', 'J', '|'}:
                colisions+=1
        #hit a pipe
print(total)
        
