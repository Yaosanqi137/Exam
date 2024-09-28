# 如果不止是检测个位数又应该怎么样呢？
# 或许可以使用字典来实现

def counter(numList):
    numDict = {}
    for checkNum in numList:
        if checkNum in numDict:
            numDict[checkNum] += 1 # 再次检测到某个数字后，对应的值加一
        else:
            numDict[checkNum] = 1 # 首次检测到某个数字时，新建对应的键
    for num, amount in numDict.items(): # 遍历字典键值对
        print(f"{num}:{amount}", end=" ")

if __name__ == '__main__':
    myList = list(map(int, input().rstrip().split())) # 输入空格分开的字符串，将其转换为整数型列表
    counter(myList)