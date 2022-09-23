# Colours Code:-

with open("//Users/Lavanya/Desktop/Man Assesments/colours.txt", "r") as colorsFile:
# 1.Which colour appears most in the file?
# 2.Which colour appears in the fewest number of lines?
# 3.How many lines contains GREEN but not BLUE?
# 4.How many lines have the same colour repeated three times?
# 5.How many lines have three different colours present?
# 6.How many lines contain atleast one colour pair in alphabetical order?

    colorsList = [line.rstrip() for line in colorsFile]
    
    count = 1
    fewestCount = len(colorsList)
    repatedColor = "No Color Is Repeated."
    fewestColor = colorsList[1]
    greenButNotBlueCount = 0
    repeatedThreeTimesCount = 0
    differntColoursCount = 0
    oneColourPairAlphaCount = 0

    for i in range(0, len(colorsList)):
        numberCount = colorsList.count(colorsList[i])
        if numberCount > count:
            count = numberCount
            repatedColor = colorsList[i]
        
        if numberCount < fewestCount:
            fewestCount = numberCount
            fewestColor = colorsList[i]

        colList = colorsList[i].split(",")
        if "GREEN" in colList and "BLUE" not in colList:
            greenButNotBlueCount += 1

        if colList[0] == colList[1] == colList[2]:
            repeatedThreeTimesCount += 1

        if (colList[0] != colList[1]) and (colList[0] != colList[2]) and (colList[1] != colList[2]):
            differntColoursCount += 1

        if (ord(colList[0][0]) < ord(colList[1][0])) or (ord(colList[1][0]) < ord(colList[2][0])):
            oneColourPairAlphaCount += 1
        
    print("Repeated Color :", repatedColor, " Count :", count)
    print("Fewest Color :", fewestColor, " Count :", fewestCount)
    print("GREEN but not BLUE :", greenButNotBlueCount)
    print("Same Colour Repeated Three Times :", repeatedThreeTimesCount)
    print("Three Different Colours Present: ",differntColoursCount)
    print("Atleast one colour pair in alphabetical order", oneColourPairAlphaCount)
