import itertools

def generateExercList():
    with open("11.txt") as file:
        lines=[]
        for line in file:
            exersNums = []
            eachNum=line.split(", ")
            for i in range(len(eachNum)):
                exersNums.append(int(eachNum[i].strip()))
            lines.append(exersNums)
    return lines
    

def getFinalList(lstInOrder,allList):
    choosenExerc = []
    lstCombinations = list(itertools.combinations(lstInOrder,4))
    for i in range(len(lstCombinations)):
            allCombinationsOfChoosenLst = list(itertools.permutations(lstCombinations[i],4))
            for k in range(len(allCombinationsOfChoosenLst)):
                if list(allCombinationsOfChoosenLst[k]) in allList:
                    allList.remove(list(allCombinationsOfChoosenLst[k]))
                    choosenExerc = list(allCombinationsOfChoosenLst[k])
                    return allList, choosenExerc
    return allList, choosenExerc        


allList = generateExercList()


while 1:
    inputNumbers = input("Παρακαλώ εισάγετε 6 αριθμούς απο το 1 έως το 14 χωρισμένους μόνο με κόμμα.")
    inputNumbers = inputNumbers.split(",")
    inputNumbers = list(map(int, inputNumbers))
    allList, selectedExer = getFinalList(inputNumbers,allList)
    if len(selectedExer) == 0:
        print("Δεν υπάρχει διαθέσιμη τετράδα.")
    else:
        print("Υπάρχει διαθέσιμη τετράδα και είναι η: ",selectedExer)
