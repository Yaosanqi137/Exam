def counter(numList):
    for checkNum in range(0, 10):
        amount = 0
        for n in numList:
            if n == checkNum :
                amount += 1
        if amount != 0:
            print(f"{checkNum}:{amount}", end=' ')

if __name__ == '__main__':
    myList = list(map(int, input().rstrip().split())) # 输入空格分开的字符串，将其转换为整数型列表
    counter(myList)