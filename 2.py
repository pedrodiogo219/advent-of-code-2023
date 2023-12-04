#12 red cubes, 13 green cubes, and 14 blue cubes?
limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

maxes = {
    "red": 0,
    "green": 0,
    "blue": 0
}

def isMeasurementValid(measurements):
    for m in measurements:
        count, color = m.split()
        # if int(count) > limits[color]:
        #     return False
        
        maxes[color] = max(int(count), maxes[color])

    return True

def allChecksAreValid(checks):
    for check in checks:
        measurements = check.split(",")
        isMeasurementValid(measurements)
        # if not isMeasurementValid(measurements):
        #     return False
    return True

with open('inputs/2.txt', 'r') as file:
    id = 0
    total = 0
    totalPower = 0
    for line in file:
        id+=1
        checks = line.strip().split(':')[1]
        checks = checks.split(';')
        if allChecksAreValid(checks):
            total += id
        
        power = maxes["red"] * maxes["blue"] * maxes["green"]
        totalPower += power
        
        maxes = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
    print(total)
    print(totalPower)