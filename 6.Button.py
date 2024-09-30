if __name__ == '__main__':
    buttonLine, clickLine = map(int, input().split()) # 获取按钮个数、点击次数
    buttons, clicks = [], [] # 定义存储按钮和点击位置信息的列表
    for n in range(buttonLine):
        button = list(map(int, input().split())) # 逐个录入按钮位置
        button.append(n + 1) # 设置按钮 ID
        buttons.append(button) # 将每个按钮位置子列表添加到按钮位置列表中
    for n in range(clickLine):
        clicks.append(list(map(int, input().split()))) # 逐个录入点击位置
    buttons.reverse() # 反转按钮位置存储列表

    for click in range(0, clickLine):
        for layer in range(0, buttonLine):
            if buttons[layer][0] <= clicks[click][0] <= buttons[layer][2] and buttons[layer][1] <= clicks[click][1] <= buttons[layer][3] : # 在第 n 次点击时，从上层往下层检查按钮是否被点击到
                print(buttons[layer][4]) # 如果点击到就输出按钮对应的 ID
                buttons.insert(0, buttons.pop(layer)) # 然后将此按钮重新插到最上层
                break # 既然已经按到按钮就不用继续往下层检查了，开始下一次点击
            elif layer == buttonLine - 1 : # 如果到最底层了也没有点击到按钮，则输出 None
                print(None)