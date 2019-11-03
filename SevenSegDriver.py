# 172.23.20.210
# from gpiozero.pins.rpigpio import RPiGPIOFactory
from gpiozero import LED, Device

# factory = Device.pin_factory()

# pin 12
first_activator = LED(11)

# pin 9
second_activator = LED(27)

# pin 8
third_activator = LED(17)

# pin 6
fourth_activator = LED(24)

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

zero = [True, True, True, False, True, True, True, False]
one = [False, False, True, False, False, True, False, False]
two = [True, False, True, True, True, False, True, False]
three = [True, False, True, True, False, True, True, False]
four = [False, True, True, True, False, True, False, False]
five = [True, True, False, True, False, True, True, False]
six = [False, True, False, True, True, True, True, False]
seven = [True, False, True, False, False, True, False, False]
eight = [True, True, True, True, True, True, True, True]
nine = [True, True, True, True, False, True, False, False]

numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

def render(number):
    newState = numbers[number]

    for i in len(gpio_order):
        if status[i] != newState[i]:
            status[i] = not status[i]
            gpio_order[i].toggle()

