def main():
    lines = open("day2.txt", "r")
    gameScores = []
    power = 0

    for x, line in enumerate(lines):
        gameNumEnd = line.find(":")
        gameScores.append({"red":0, "blue":0, "green":0})

        cubes = line[gameNumEnd+1:]
        games = cubes.split(";")
        for game in games:
            if game[-1] == "\n":
                game = game[:-1]
            for color in ["red", "blue", "green"]:
                numEnd = game.find(f"{color}") - 1
                if numEnd == -2:
                    continue
                offset = game[numEnd - 1::-1].find(" ")
                score = game[numEnd - offset:numEnd:]
                
                if gameScores[x][color] < int(score):
                    gameScores[x][color] = int(score)

            
        power += gameScores[x]["red"] * gameScores[x]["green"] * gameScores[x]["blue"]
        
    print(power)

if __name__ == "__main__":
    main()