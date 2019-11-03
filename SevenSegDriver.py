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
bottom_left = LED(8)

#pin 4
bottom_right = LED(16)

#pin 2
bottom = LED(12)

#pin_3
seperator = LED(7)

#pin 5
center = LED(25)
