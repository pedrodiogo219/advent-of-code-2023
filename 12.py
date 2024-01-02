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

memo = {}

def dp(pos, groupPos, last):
    if groupPos > len(groups):
        return 0
    if pos == len(springs):
        memo[(pos, groupPos, last)] = int(groupPos == len(groups))
        return memo[(pos, groupPos, last)]
    if (pos, groupPos, last) in memo:
        return memo[(pos, groupPos, last)]
    
    # print((pos, groupPos, last))
    # print("analisando um ", springs[pos])
    ans = 0
    if springs[pos] == '.' or springs[pos] == '?':
        if last > 0:
            if groupPos >= len(groups) or last != groups[groupPos]:
                ans = 0
            else:
                ans += dp(pos + 1, groupPos + 1, 0)
        else:
            ans += dp(pos + 1, groupPos, 0)

    if springs[pos] == '#' or springs[pos] == '?':
        ans += dp(pos + 1, groupPos, last + 1)            
    
    memo[(pos, groupPos, last)] = ans
    return ans

with open('inputs/12.txt', 'r') as file:
    lineCount = 0
    m = 0
    total = 0
    for line in file:
        springs, groups = line.strip().split()
        groups = list(map(int, groups.split(',')))

        aux = springs
        for _ in range(4):
            springs += '?' + aux
        springs += '.'

        naux = [g for g in groups]
        for _ in range(4):
            groups += naux

        memo = {}
        ans = dp(0, 0, 0)
        print(ans)
        # print(memo)
        total += ans
    print(total)
    

