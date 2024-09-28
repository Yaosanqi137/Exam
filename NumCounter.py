def counter(numList):
    for checkNum in range(0, 10):
        amount = 0
        for n in numList:
            if n == checkNum :
                amount += 1
        if amount != 0:
            print(f"{checkNum}:{amount}", end=' ')

if __name__ == '__main__':
    elementInput = str(input())
    myList = elementInput.split()
    for i in range(0, len(myList)):
        myList[i] = int(myList[i])
    counter(myList)