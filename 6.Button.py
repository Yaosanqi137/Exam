if __name__ == '__main__':
    buttonLine, clickLine = map(int, input().split())
    buttons, clicks = [], []
    for n in range(buttonLine):
        button = list(map(int, input().split()))
        button.append(n + 1)
        buttons.append(button)
    for n in range(clickLine):
        clicks.append(list(map(int, input().split())))
    buttons.reverse()

    for click in range(0, clickLine):
        for layer in range(0, buttonLine):
            if buttons[layer][0] <= clicks[click][0] <= buttons[layer][2] and buttons[layer][1] <= clicks[click][1] <= buttons[layer][3] :
                print(buttons[layer][4])
                buttons.insert(0, buttons.pop(layer))
                break
            elif layer == buttonLine - 1 :
                print(None)