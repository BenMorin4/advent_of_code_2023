import math

def main():
    with open("day4.txt", "r") as file:
        ans = 0
        lines = file.readlines()
        copiesOfCard = [1 for _ in range(len(lines))]
        for row, line in enumerate(lines):
            scored = False
            for _ in range(int(copiesOfCard[row])):
                if scored == True:
                    ans += 1
                    continue
                cardScore = 0
                winningNumbers = []
                card = line[line.find(":")+1:].strip()
                for num in card[card.find("|")+1:].strip().split(" "):
                    if not num == "":
                        winningNumbers.append(num)
                for num in card[:card.find("|")].strip().split(" "):
                    if not num == "":
                        if num in winningNumbers:
                            if cardScore == 0:
                                cardScore = 1
                            else:
                                cardScore = cardScore * 2
                scored = True
                ans += 1

            if not cardScore == 0:
                for count in range(int(math.log(cardScore, 2)) + 1):
                    #print(range(int(math.log(cardScore, 2))))
                    try:
                        copiesOfCard[row + 1 + count] += (1 * copiesOfCard[row])
                    except IndexError:
                        continue
            
        print(ans)
                    




if __name__ == "__main__":
    main()