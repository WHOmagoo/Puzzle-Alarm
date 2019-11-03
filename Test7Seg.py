import time
import SevenSegDriver



def test_on(activator, s):
    s.first_activator.on()
    s.second_activator.on()
    s.third_activator.on()
    s.fourth_activator.on()
    
    if activator == 1:
        s.first_activator.off()
    elif activator == 2:
        s.second_activator.off()
    elif activator == 3:
        s.third_activator.off()
    elif activator == 4:
        s.fourth_activator.off()

def test_all_segments(s):
    s.top_seg.off()
    s.top_left.off()
    s.top_right.off()
    s.center_seg.off()
    s.bottom_left.off()
    s.bottom_right.off()
    s.bottom_seg.off()
    s.seperator.off()

    time.sleep(.5)
    s.top_seg.on()
    time.sleep(.5)
    s.top_left.on()
    time.sleep(.5)
    s.top_right.on()
    time.sleep(.5)
    s.center_seg.on()
    time.sleep(.5)
    s.bottom_left.on()
    time.sleep(.5)
    s.bottom_right.on()
    time.sleep(.5)
    s.bottom_seg.on()
    time.sleep(.5)
    s.seperator.on()
    time.sleep(.5)

def test_gpio_connections(s):
    for i in range(4):
        print("Testing panel ", i)
        test_on(i+1, s)
        test_all_segments(s)

def test_panel_render(s):
    s.set_display([1,4,5,7])
    while True:
        s.render_display()



def test_number_display(s):
    s.first_activator.on()
    s.second_activator.on()
    s.third_activator.on()
    while True:
        for i in range(10):
            s.render_single_number(i)
            time.sleep(.75)


if __name__ == '__main__':
    # test_gpio_connections()
    # test_number_display()
    s = SevenSegDriver.SevenSegDrive()
    test_panel_render(s)