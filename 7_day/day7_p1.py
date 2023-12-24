cardValues = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
scores = {"5 of a kind": 7, "4 of a kind": 6, "Full house": 5, "3 of a kind": 4, "Two pair": 3, "One pair": 2, "High card": 1}

def main():
    with open("day7.txt", "r") as file:
        lines = file.readlines()
        ranksAndBids = []

        print('before')
        for lineNum, line in enumerate(lines):
            print('in')
            cards = line.split(" ")[0].strip()
            bid = line.split(" ")[1].strip()
            
            rank = []
            hand = {}
            for card in list(cards):
                hand[card] = hand.get(card, 0) + 1
                rank.append(cardValues[card])

            numOfCards = []
            for numOfCard in hand.values():
                numOfCards.append(numOfCard)
            numOfCards.sort()
            numOfCards = numOfCards[::-1]

            if numOfCards[0] == 5:
                rank.insert(0, scores["5 of a kind"])
            elif numOfCards[0] == 4:
                rank.insert(0, scores["4 of a kind"])
            elif numOfCards[0] == 3:
                if numOfCards[1] == 2:
                    rank.insert(0, scores["Full house"])
                else: 
                    rank.insert(0, scores["3 of a kind"])
            elif numOfCards[0] == 2:
                if numOfCards[1] == 2:
                    rank.insert(0, scores["Two pair"])
                else:
                    rank.insert(0, scores["One pair"])
            else:
                rank.insert(0, scores["High card"])
            
            ranksAndBids.append({'rank': rank, 'bid': bid})

        sortedHands = sorted(ranksAndBids, key=lambda x: (x['rank'][0], x['rank'][1], x['rank'][2], x['rank'][3], x['rank'][4], x['rank'][5]), reverse=True)

        print(sortedHands)

        ans = 0
        rank = len(sortedHands)
        for hand in sortedHands:
            bid = hand['bid']
            print(ans, rank, bid)
            ans += ((rank) * int(bid))
            rank-=1

        print(ans)

if __name__ == "__main__":
    main()