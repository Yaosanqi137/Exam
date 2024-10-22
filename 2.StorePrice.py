def price(amount, priceList):
    backup = priceList[:] # 创建副本列表
    for n in range(0, amount):
        if n - 1 == -1:
            priceList[n] = (backup[n] + backup[n + 1]) // 2 # 对第一个店铺价格的处理
        elif n + 1 == amount:
            priceList[n] = (backup[n - 1] + backup[n]) // 2 # 对最后一个店铺价格的处理
        else:
            priceList[n] = (backup[n - 1] + backup[n] + backup[n + 1]) // 3 # 对其他店铺价格的处理
        print(priceList[n],end=" ")

if __name__ == '__main__':
    storeAmount = int(input())
    myPriceList = list(map(int, input().split()))
    price(storeAmount, myPriceList)
