with open('inputs/5.txt', 'r') as file:
    line = file.readline()
    seeds = list(map(int, line.strip().split()[1:]))
    blankLine = file.readline()

    intervals = []
    for seedStart, seedRange in zip(seeds[0::2], seeds[1::2]):
        intervals.append((seedStart, seedStart+seedRange))

    def readMap(intervals):
        header = file.readline()
        header = header.strip().split()[0]
        
        newIntervals = []
        while True:
            line = file.readline()
            if not line or line == "\n":
                break

            destinationRangeStart, sourceRangeStart, rangeLength = list(map(int, line.strip().split()))
            c = sourceRangeStart
            d = sourceRangeStart + rangeLength

            difference = destinationRangeStart - sourceRangeStart

            leftovers = []
            while len(intervals):
                a, b = intervals.pop()

                # SEED RANGE =       [a                             b)
                # MAPPING RANGE =               [c        d)  
                # results =           [before)    [inside)   [after) 
                before = (a,         min(b, c))
                inside = (max(a, c), min(b, d))
                after  = (max(a, d), b)
                
                # check if they are valid intervals
                if before[0] < before[1]:
                    leftovers.append(before)
                if inside[0] < inside[1]:
                    newIntervals.append((inside[0] + difference, inside[1] + difference))
                if after[0] < after[1]:
                    leftovers.append(after)            

            intervals = leftovers
        
        intervals = newIntervals + intervals
        return intervals

    for _ in range(7):
        intervals = readMap(intervals)

    minAns = intervals[0][0]
    for interval in intervals:
        if interval[0] < minAns:
            minAns = interval[0]

    print(minAns)