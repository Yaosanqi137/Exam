def errCatch(buttonInput, clickInput): # 异常输入检测
    for checkButton in buttonInput:
        if len(checkButton) != 5:
            print("注意!错误的按钮坐标输入,应该为(x1 y1 x2 y2)请重新输入数据:")
            return False
        else:
            if checkButton[0] >= checkButton[2] or checkButton[1] >= checkButton[3]:
                print("注意按钮坐标输入格式!应该为(x1 <  x2,y1 < y2),请重新输入数据:")
                return False
            else:
                for i in range(0, 4):
                    if checkButton < 0 or checkButton > 1000 :
                        return False
                return True
    for checkClick in clickInput:
        if len(checkClick) != 2:
            print("注意!错误的点击坐标输入,应该为(x y),请重新输入数据:")
            return False
        else:
            for j in range(0, 1):
                if checkClick[j] < 0 or checkClick[j] > 1000 :
                    return False
            return True

if __name__ == '__main__':
    while 1 : # 只有在输入了正确的数据的时候才会跳出循环,不然一直重新输入数据
        buttonLine, clickLine = map(int, input().split())  # 获取按钮个数、点击次数
        if buttonLine < 1 or buttonLine > 10:
            print("注意!按钮数量应该在 1 到 10 之间,请重新输入数据:")
            continue
        if clickLine < 1 or clickLine > 10:
            print("注意!点击次数应该在 1 到 10 之间,请重新输入数据:")
            continue
        buttons, clicks = [], []  # 定义存储按钮和点击位置信息的列表
        for n in range(buttonLine):
            button = list(map(int, input().split()))  # 逐个录入按钮位置
            button.append(n + 1)  # 设置按钮 ID
            buttons.append(button)  # 将每个按钮位置子列表添加到按钮位置列表中
        for n in range(clickLine):
            clicks.append(list(map(int, input().split())))  # 逐个录入点击位置
        buttons.reverse()  # 反转按钮位置存储列表
        if errCatch(buttons, clicks):
            break

    # 数据处理及输出段
    for click in range(0, clickLine):
        for layer in range(0, buttonLine):
            if buttons[layer][0] <= clicks[click][0] <= buttons[layer][2] and buttons[layer][1] <= clicks[click][1] <= buttons[layer][3] : # 在第 n 次点击时，从上层往下层检查按钮是否被点击到
                print(buttons[layer][4]) # 如果点击到就输出按钮对应的 ID
                buttons.insert(0, buttons.pop(layer)) # 然后将此按钮重新插到最上层
                break # 既然已经按到按钮就不用继续往下层检查了，开始下一次点击
            elif layer == buttonLine - 1 : # 如果到最底层了也没有点击到按钮，则输出 None
                print(None)