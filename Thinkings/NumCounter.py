# 如果不止是检测个位数又应该怎么样呢？
# 或许可以使用字典来实现

def counter(numList):
    numDict = {}
    for checkNum in numList:
        if checkNum in numDict:
            numDict[checkNum] += 1
        else:
            numDict[checkNum] = 1
    for num, amount in numDict.items(): # 遍历字典
        print(f"{num}:{amount}", end=" ")

if __name__ == '__main__':
    elementInput = str(input())
    myList = elementInput.split()
    for i in range(0, len(myList)):
        myList[i] = int(myList[i])
    counter(myList)