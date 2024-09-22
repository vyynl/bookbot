def main():
    txtPath = 'books/frankenstein.txt'
    text = getText(txtPath)
    wordCount = getWordCount(text)
    charsDict = getCharCounts(text)

    print(f"--- Begin report of {txtPath} ---")
    print(f"{wordCount} words found in the document\n")

    sortedByCount = sorted(charsDict, key=charsDict.get, reverse=True)
    for i in range(len(sortedByCount)):
        char = sortedByCount[i]
        if char.isalpha():
            print(f"The '{char}' character was found {charsDict[char]} times")

def getText(txtPath):
    with open(txtPath) as f:
        return f.read()

def getWordCount(text):
    return len(text)

def getCharCounts(text):
    charDict = {}
    for char in text.lower():
        if char not in charDict:
            charDict[char] = 0
        charDict[char] += 1
    return charDict

main()