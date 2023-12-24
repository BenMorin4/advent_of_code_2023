def main():
    with open("day4.txt", "r") as file:
        ans = 0
        lines = file.readlines()
        for row, line in enumerate(lines):
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
            ans += cardScore            
        print(ans)
                    




if __name__ == "__main__":
    main()