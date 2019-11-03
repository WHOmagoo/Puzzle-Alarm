import time
import SevenSegDriver as s

if __name__ == '__main__':
    s.first_activator.on()
    s.second_activator.on()
    s.third_activator.on()
    s.fourth_activator.off()

    s.top_seg.on()
    time.sleep(.5)
    s.top_left.on()
    time.sleep(.5)
    s.top_right.on()
    time.sleep(.5)
    s.center.on()
    time.sleep(.5)
    s.bottom_left.on()
    time.sleep(.5)
    s.bottom_right.on()
    time.sleep(.5)
    s.bottom.on()
    time.sleep(.5)
    s.seperator.on()
    time.sleep(.5)
