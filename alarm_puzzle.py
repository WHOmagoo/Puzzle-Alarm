import random
import math
class alarm_puzzle:
    display = []
    correct = 0
    solved = False

    def __init__(self):
        self.generate_puzzle()

    def is_solved(self):
        return self.solved

    def generate_puzzle(self):
        for i in range (4):
            self.display = [4,3,2,1]
            # col_num = random.random()
            # col_num = col_num * 9
            # self.display[i] = math.floor(col_num)


    def is_correct(self, button_number):
        i = button_number + 1
        n = self.correct

        return self.largest(self.correct) == self.correct[button_number]


    #def find_nth_lowest_number(self, n):
    #   self.display = [4, 7, 9, 8]

    def largest(self, n):

        # Initialize maximum element

        # Traverse array elements from second
        # and compare every element with
        # current max
        order = []
        order_index = []
        display_copy = self.display
        for i in range(5 - n):
            max = -1
            max_index = -1
            for j in range(4):
                if j in order_index:
                    continue
                else:
                    if display_copy[j] > max:
                        max = display_copy[j]
                        max_index = j

            order.append(max)
            order_index.append(max_index)

        return order.pop()
"""
    # Driver Code
         arr = [4,7,9,8]
         n = len(arr)
         Ans = largest(arr, n)
         info = 1
         print("Largest in given array is", Ans)


         n = len(arr)
         Ans = largest(arr, n)
         info = 2
         print("second Largest in given array is", Ans)

         n = len(arr)
         Ans = largest(arr, n)
         info = 3
         print("third Largest in given array is", Ans)

         arr = [4]
         n = len(arr)
         Ans = largest(arr, n)
         info = 4
         print("third Largest in given array is", Ans)
"""


def input(self):

    value = input("Enter botton:")

    print(value)

def push_button(self, button_number):

    i = button_number

    if 0 < i < 5:
        #if self.is_correct(button_number):
        self.correct += 1
    else:
        self.correct = 0
    self.solved = self.correct == 4

    return self.solved





"""
# code modified, tweaked and tailored from code by bertwert
# on RPi forum thread topic 91796
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO ports for the 7seg pins
segments = (11, 4, 23, 8, 7, 10, 18, 25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

# GPIO ports for the digit 0-3 pins
digits = (22, 27, 17, 24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

num = {' ': (0, 0, 0, 0, 0, 0, 0),
       '0': (1, 1, 1, 1, 1, 1, 0),
       '1': (0, 1, 1, 0, 0, 0, 0),
       '2': (1, 1, 0, 1, 1, 0, 1),
       '3': (1, 1, 1, 1, 0, 0, 1),
       '4': (0, 1, 1, 0, 0, 1, 1),
       '5': (1, 0, 1, 1, 0, 1, 1),
       '6': (1, 0, 1, 1, 1, 1, 1),
       '7': (1, 1, 1, 0, 0, 0, 0),
       '8': (1, 1, 1, 1, 1, 1, 1),
       '9': (1, 1, 1, 1, 0, 1, 1)}

try:
    while True:
        n = time.ctime()[11:13] + time.ctime()[14:16]
        s = str(n).rjust(4)
        for digit in range(4):
            for loop in range(0, 7):
                GPIO.output(segments[loop], num[s[digit]][loop])
                if (int(time.ctime()[18:19]) % 2 == 0) and (digit == 1):
                    GPIO.output(25, 1)
                else:
                    GPIO.output(25, 0)
            GPIO.output(digits[digit], 0)
            time.sleep(0.001)
            GPIO.output(digits[digit], 1)
finally:
    GPIO.cleanup()
"""



