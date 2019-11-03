# 172.23.20.210
# from gpiozero.pins.rpigpio import RPiGPIOFactory
from gpiozero import LED
from threading import Thread
import time
import TimeToArray

# factory = Device.pin_factory()
class SevenSegDrive:
    # pin 12
    first_activator = LED(11)
    first_activator.off()

    # pin 9
    second_activator = LED(27)
    second_activator.on()

    # pin 8
    third_activator = LED(17)
    third_activator.on()

    # pin 6
    fourth_activator = LED(24)
    fourth_activator.on()

    # pin 11
    top_seg = LED(10)

    #pin 10
    top_left = LED(22)

    #pin 7
    top_right = LED(4)

    #pin 1
    bottom_left = LED(16)

    #pin 4
    bottom_right = LED(8)

    #pin 2
    bottom_seg = LED(12)

    #pin_3
    seperator = LED(7)

    #pin 5
    center_seg = LED(25)

    gpio_order = [top_seg, top_left, top_right, center_seg, bottom_left, bottom_right, bottom_seg, seperator]

    status = [False,False,False,False,False,False,False,False, False]

    digit_status = [True, False, False, False]
    digits = [first_activator, second_activator, third_activator, fourth_activator]

    zero = [True, True, True, False, True, True, True, False]
    one = [False, False, True, False, False, True, False, False]
    two = [True, False, True, True, True, False, True, False]
    three = [True, False, True, True, False, True, True, False]
    four = [False, True, True, True, False, True, False, False]
    five = [True, True, False, True, False, True, True, False]
    six = [False, True, False, True, True, True, True, False]
    seven = [True, False, True, False, False, True, False, False]
    eight = [True, True, True, True, True, True, True, False]
    nine = [True, True, True, True, False, True, False, False]

    numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

    display = [0,0,0,0]

    cur_digit = 0

    thread = None

    def __init__(self, time):
        self.set_display(time)
        self.thread = Thread(target=self.render_forever)
        self.thread.start()


    def set_display(self, new_display):
        self.display = new_display

    def enable_seperator(self):
        self.status[7] = True

    def disable_seperator(self):
        self.status[7] = False

    def set_cur_digit_output(self, new_digit):
        if self.cur_digit != new_digit:
            self.digit_status[self.cur_digit] = False
            self.digits[self.cur_digit].on()
            self.digit_status[new_digit] = True
            self.digits[new_digit].off()
            self.cur_digit = new_digit


    def off(self):
        for index, value in enumerate(self.status):
            if value is True:
                self.gpio_order[index].off()

        self.status = [False] * 8


    def render_forever(self):
        while True:
            self.render_display()

    def render_display(self):
        for i in range(4):
            if i == 0 and self.display[i] == 0:
                continue

            self.set_cur_digit_output(i)
            self.render_single_number(self.display[i])
            time.sleep(.5)
            self.off()
            time.sleep(.5)


    def notify(self, sender):
        newTime = TimeToArray.time_to_array(sender.get_time().time())
        self.set_display(newTime)

    def render_single_number(self, number):
        newState = self.numbers[number]

        for i in range(len(self.gpio_order)):
            if self.status[i] != newState[i]:
                self.status[i] = not self.status[i]
                self.gpio_order[i].toggle()

        if self.cur_digit == 1:
            self.enable_seperator()
        else:
            self.disable_seperator()

