def main():
    lines = open("day1.txt", "r")
    total = 0
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    keys = []
    for key in words:
        keys.append(key)

    for line in lines:
        done = False
        possibleWords = {}
        for char in line:
            if done == True:
                break

            if char.isnumeric():
                x = char
                break

            if not possibleWords == {}:
                for word, indexes in possibleWords.copy().items():
                    if (indexes):
                        for index in indexes:
                            if (char == word[index]) and (len(word) - 1 == index):
                                x = words[word]
                                done = True
                                break
                            elif char == word[index]:
                                newIndexes = indexes
                                newIndexes.remove(index)
                                newIndexes.append(index + 1)
                                possibleWords[word] = newIndexes      
                            else:
                                newIndexes = indexes
                                newIndexes.remove(index)
                                if newIndexes == []:
                                    del possibleWords[word]
                                else:
                                    possibleWords[word] = newIndexes

            for key in keys:
                if char == key[0]:
                    possibleWords[key] = possibleWords.get(key, [])
                    possibleWords[key].append(1)

        # go backwards
        done = False
        possibleWords = {}
        for char in line[::-1]:
            if done == True:
                break

            if char.isnumeric():
                y = char
                break

            if not possibleWords == {}:
                for word, indexes in possibleWords.copy().items():
                    if (indexes):
                        for index in indexes.copy():
                            if (char == word[index]) and (0 == index):                            
                                y = words[word]
                                done = True
                                break
                            elif char == word[index]:
                                newIndexes = indexes
                                newIndexes.remove(index)
                                newIndexes.append(index - 1)
                                possibleWords[word] = newIndexes      
                            else:
                                newIndexes = indexes
                                newIndexes.remove(index)
                                if newIndexes == []:
                                    del possibleWords[word]
                                else:
                                    possibleWords[word] = newIndexes

            for key in keys:
                if char == key[len(key) - 1]:
                    possibleWords[key] = possibleWords.get(key, [])
                    possibleWords[key].append(len(key) - 2)

        total += int(str(x) + str(y))
    print('total', total)      

if __name__ == "__main__":
    main()
