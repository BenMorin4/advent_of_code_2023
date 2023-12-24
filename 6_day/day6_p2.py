def main():
    waysToWin = []

    with open("day6.txt", "r") as file:
        lines = file.readlines()

        # turn the lines into numbers
        time = int(''.join(lines[0][5:].strip().split("     ")))
        record = int(''.join(lines[1][9:].strip().split("   ")))

        waysToWinThisRace = 0
        for trial in range(time):
            distance = trial * (time - trial)
            if distance > record:
                waysToWinThisRace += 1
        
        print(waysToWinThisRace)
    

if __name__ == "__main__":
    main()