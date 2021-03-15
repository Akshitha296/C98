# test = open("FunctionTest.txt")
# test.read()
# fileLines = test.readlines()
# for lines in fileLines: 
#     print(lines)
# introString = "My name is Y/N. I go to unnamed school. And just oink."
# introString.split("a")

def fileWordCount():
    fileName = input("What is your file name?")
    file = open(fileName)
    numberOfWords = 0
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords+len(words)
    print(numberOfWords)