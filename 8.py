import re, math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

graph = {}
As = []
Zs = []
with open('inputs/8.txt', 'r') as file:
    steps = file.readline().strip()
    blankLine = file.readline()

    while True:
        line = file.readline()
        if not line or line == "\n":
            break
        
        node, left, right = re.compile(r'[A-Z0-9]{3}').findall(line)
        graph[node] = {
            'L': left,
            'R': right
        }

        if node[-1] == 'A':
            As.append(node)
        if node[-1] == 'Z':
            Zs.append(node)

ans = 1
for pos in As:
    memo = {}
    cont = 0
    idx = 0

    while True:
        if pos in memo: 
            if idx in memo[pos]:
                cycleSize = cont - memo[pos][idx]
                print("cycle size: ", cycleSize)
                ans = lcm(ans, cycleSize)
                break
        else:
            memo[pos] = {}
        memo[pos][idx] = cont

        pos = graph[pos][steps[idx]]

        cont += 1
        idx = (idx + 1) % len(steps)

    # print(memo)
print(ans)