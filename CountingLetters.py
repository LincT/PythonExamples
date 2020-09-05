def letterTypeCount(myString):  # vowel and consonant counts
    vowels = "aeiou"
    consonantString = ""
    vowelString = ""
    returnData = []
    for char in myString:
        if str(char).lower().isalpha() and str(char).lower() not in vowels:
            consonantString += char
        elif str(char).lower() in vowels:
            vowelString += char
    returnData.append("Vowels: " + str(len(vowelString)))
    returnData.append("Consonants: " + str(len(consonantString)))
    return returnData


def readLines():  # read lines in a file and get statistics
    readFile = open(r".\sample_data\text.txt")
    wordcount = 0
    lines = readFile.readlines()
    for line in lines:
        wordcount += len(line.split())
        print("Words in line: " + str(len(line.split())) + "\n\t" + str(letterTypeCount(line.strip("\n"))[0])
              + "\n\t" + str(letterTypeCount(line.strip("\n"))[1]))
    print("Total words: " + str(wordcount))


def main():
    readLines()


main()
