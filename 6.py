import math
with open('inputs/6.txt', 'r') as file:

    time = int("".join(file.readline().strip().split()[1:]))
    distance = int("".join(file.readline().strip().split()[1:]))
    
    print(time, distance)

    delta = math.sqrt((time*time) - (4)*(-1)*(-distance))
    
    A = math.ceil((-time + delta) / -2)
    B = math.floor((-time - delta) / -2)

    print(A, B)
    print(B - A + 1)    