def lcm(num1, num2):
    check = max(num1, num2)
    while True:
        if check % num1 == 0 and check % num2 == 0 :
            break
        else:
            check += 1
    return check

def matrix(order):
    columnList = []
    for column in range(1,order + 1):
        lineList = []
        for line in range(1,order + 1):
            lineList.append(lcm(line, column))
        columnList.append(lineList)
    for i in range(0, len(columnList)):
        for j in range(0, len(columnList[i])):
            print(columnList[i][j], end="   ")
        print("\n")

if __name__ == '__main__':
    n = int(input())
    matrix(n)