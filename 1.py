def isDigit(c):
    return '0' <= c and c <= '9'

def filterDigits(s):
    if len(s) < 1:
        return []
    final = []
    if isDigit(s[0]):
        final.append(int(s[0]))
    elif s[0:3] == "one":
        final.append(1)
    elif s[0:3] == "two":
        final.append(2)
    elif s[0:5] == "three":
        final.append(3)
    elif s[0:4] == "four":
        final.append(4)
    elif s[0:4] == "five":
        final.append(5)
    elif s[0:3] == "six":
        final.append(6)
    elif s[0:5] == "seven":
        final.append(7)
    elif s[0:5] == "eight":
        final.append(8)
    elif s[0:4] == "nine":
        final.append(9)

    final += filterDigits(s[1:])
    return final

total = 0
with open('inputs/1.txt', 'r') as file:
    for line in file:
        numbers = filterDigits(line)
        calibrationValue = numbers[0]*10 + numbers[-1]
        total+=calibrationValue
    print(total)