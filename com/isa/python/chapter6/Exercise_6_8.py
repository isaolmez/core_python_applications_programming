digitDictionary = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six",
                   "7": "seven", "8": "eight", "9": "nine"}


def englishWord(num):
    numString = str(num)
    return "-".join([digitDictionary.get(digitString) for digitString in numString])


print englishWord(90283)

digitDictionary = {"0": ["zero", "", ""],
                   "1": ["one", "ten", "hundred"],
                   "2": ["two", "twenty", "two hundred"],
                   "3": ["three", "thirty", "three hundred"],
                   "4": ["four", "forty", "four hundred"],
                   "5": ["five", "fifty", "five hundred"],
                   "6": ["six", "sixty", "six hundred"],
                   "7": ["seven", "seventy", "seven hundred"],
                   "8": ["eight", "eighty", "eight hundred"],
                   "9": ["nine", "ninety", "nine hundred"]}


def englishWordAdvanced(num):
    numString = str(num)
    length = len(numString)
    i = 0
    outputList = []
    while i < length:
        outputList.append(digitDictionary.get(numString[i])[length - 1 - i])
        i += 1

    return "-".join(outputList)


print englishWordAdvanced(867)
