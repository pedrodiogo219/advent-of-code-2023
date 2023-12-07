translate = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1
}

class Hand:
    def __init__(self, cards, bid):
        self.cards = list(map(lambda x: translate[x], cards))
        self.bid = int(bid)

        self.cards_comparable = "".join(
            list(map(lambda x: chr(ord('a') + x - 1), self.cards))
        )

        counter = {}
        for key in translate.values():
            counter[key] = 0
        
        self.biggest = 0
        idx = -1
        jokers = 0
        for i in range(len(self.cards)):
            card = self.cards[i]
            if card == 1:
                jokers += 1
                continue
            counter[card] += 1
            if counter[card] > self.biggest:
                self.biggest = counter[card]
                idx = i

        self.biggest += jokers
        counter[self.cards[idx]] = 0
        self.secondBiggest = max(counter.values())

    def __lt__(self, other):
        if self.biggest != other.biggest:
            return self.biggest < other.biggest
        elif self.secondBiggest != other.secondBiggest:
            return self.secondBiggest < other.secondBiggest
        else:
            return self.cards_comparable < other.cards_comparable

hands = []

with open('inputs/7.txt', 'r') as file:
    for line in file:
        cards, bid = line.strip().split()
        hands.append(Hand(cards, bid))


hands.sort()
total = 0
i = 0
for hand in hands:
    i+=1
    # print(hand.cards, hand.bid, hand.biggest, hand.secondBiggest)
    total += hand.bid * i
print(total)