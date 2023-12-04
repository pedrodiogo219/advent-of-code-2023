with open('inputs/4.txt', 'r') as file:
    total = 0
    for line in file:
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
    print(total)


