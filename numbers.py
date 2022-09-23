# Numbers Code:-

with open("/Users/Lavanya/Desktop/Man Assesments/numbers.txt", "r") as numbersFile:
# 1.Which digit appears most in the file?
# 2.Which number is missing?

    numbersList = [int(line.rstrip()) for line in numbersFile]
   
    count = 1
    repatedNumber = "No Number Is Repeated."
    missingNumber = "No Number Is Missing."
    for i in range(0, len(numbersList)):
        numberCount = numbersList.count(numbersList[i])
        if numberCount > count:
            count = numberCount
            repatedNumber = numbersList[i]

        if i not in numbersList:
            missingNumber = i
        
    print("Repeated Number :", repatedNumber, " Count :", count)
    print("Missing Number :", missingNumber)
    