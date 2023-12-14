def countQuestionMarks(line):
    count = 0
    for c in line:
        if c == '?':
            count += 1
    return count


def bruteForce(springs, groups):
    validAns = 0
    N = countQuestionMarks(springs)
    for i in range(2**N):
        binary = bin(i)[2:]
        binary = '0' * (N - len(binary)) + binary
        newSprings = springs
        for j in range(N):
            if binary[j] == '0':
                c = '.'
            else:
                c = '#'
            newSprings = newSprings.replace('?', c, 1)
        if check(newSprings, groups):
            validAns += 1
    return validAns

def check(springs, groups):
    springs += '.'
    last = '.'
    newGroups = []
    cont = 0
    for s in springs:
        if s == '.' and last == '#':
            newGroups.append(cont)
            cont = 0
        if s == '#':
            cont += 1
        last = s
    
    # print(springs, groups)
    return newGroups == groups
            

with open('inputs/12.txt', 'r') as file:
    lineCount = 0
    m = 0
    total = 0
    for line in file:
        springs, groups = line.strip().split()
        groups = list(map(int, groups.split(',')))

        ans = bruteForce(springs, groups)
        # print(ans)
        total += ans
    print(total)
    

