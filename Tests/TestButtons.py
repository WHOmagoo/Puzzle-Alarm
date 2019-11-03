import Buttons

if __name__ == '__main__':
    while True:
        if Buttons.button1.is_pressed:
            print(1)
        if Buttons.button2.is_pressed:
            print(2)
        if Buttons.button3.is_pressed:
            print(3)
        if Buttons.button4.is_pressed:
            print(4)
