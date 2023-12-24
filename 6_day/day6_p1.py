def main():
    waysToWin = []

    with open("day6.txt", "r") as file:
        lines = file.readlines()
        times = int(''.join(lines[0][5:].strip().split("     ")))
        records = int(''.join(lines[1][9:].strip().split("   ")))

        print(times, records)

        # for each race
        for raceNum, time in enumerate(times):
            waysToWinThisRace = 0

            # for each possible trial we can have with this time
            for trial in range(int(time)):
                if trial == 0: continue
                
                distance = trial * (int(time) - trial)
                if distance > int(records[raceNum]):
                    waysToWinThisRace += 1
            
            waysToWin.append(waysToWinThisRace)

    ans = 1
    for way in waysToWin:
        ans *= way
    
    print(ans)

if __name__ == "__main__":
    main()