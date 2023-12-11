with open('inputs/9.txt', 'r') as file:
    total = 0
    while True:
        seq = []
        text = file.readline().strip().split()
        seq.append(list(map(int, text))[::-1])
        if not text:
            break
        line = 0
        while True:
            newSeq = []
            stop = True
            for i in range(len(seq[line])-1):
                j = i+1
                diff = seq[line][j] - seq[line][i]
                newSeq.append(diff)
                if diff != 0:
                    stop = False
                
            line += 1
            seq.append(newSeq)
            if stop:
                break
                
            

        seq[-1].append(0)
        for line in range(len(seq)-2, -1, -1):
            seq[line].append( seq[line][-1] + seq[line+1][-1] )
        
        # print(seq)
        # print(seq[0][-1])
        total += seq[0][-1]

    print(total)


