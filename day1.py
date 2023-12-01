def main():
    lines = open("day1.txt", "r")
    total = 0
    for line in lines:

        index = 0
        for char in line:
            if char.isnumeric():
                x = char
                break

   
        for char in line [::-1]:
            if char.isnumeric():
                y = char
                break

        total += int(str(x) + str(y))
    print(total)      

if __name__ == "__main__":
    main()
