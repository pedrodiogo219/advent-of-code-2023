with open('inputs/4.txt', 'r') as file:
    total = 0
    instances = [1 for _ in range(0, 205)]
    pos = -1
    for line in file:
        pos+=1
        #ignore the first part "Card ###:"
        line = line.strip().split(':')[1]
        winningNumbers, myNumbers = line.split('|') 
        winningNumbers = set(winningNumbers.split())
        # print(winningNumbers)
        # print(myNumbers)
        myNumbers = myNumbers.split()
        corrects = 0
        for number in myNumbers:
            if number in winningNumbers:
                # print(number)
                corrects += 1
        if corrects > 0:
            total += (2**(corrects-1))
            for i in range(pos+1, pos+1+corrects):
                instances[i] += instances[pos]
        print(instances)
    print("total points: ", total)

    print("total cards: ", sum(instances))



