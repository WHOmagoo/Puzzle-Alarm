# 172.23.20.210
# from gpiozero.pins.rpigpio import RPiGPIOFactory
from gpiozero import LED
import Time

# factory = Device.pin_factory()

global cur_digit, status

# pin 12
first_activator = LED(11)
first_activator.on()

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

status = [False,False,False,False,False,False,False,False]

digit_status = [True, True, True, True]
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

def set_display(new_display):
    display = new_display

def set_cur_digit_output(new_digit):
    digit_status[cur_digit] = False
    digits[cur_digit].toggle()
    digit_status[new_digit] = True
    digits[new_digit].toggle()
    global cur_digit
    cur_digit = new_digit


def off():
    global status
    for index, value in enumerate(status):
        if value is True:
            gpio_order[index].off()

    status = [False] * 8


def render_display():
    for i in range(4):
        set_cur_digit_output(i)
        render_single_number(display[i])
        Time.sleep(.008)
        off()
        Time.sleep(.008)



def render_single_number(number):
    newState = numbers[number]

    for i in range(len(gpio_order)):
        if status[i] != newState[i]:
            status[i] = not status[i]
            gpio_order[i].toggle()

