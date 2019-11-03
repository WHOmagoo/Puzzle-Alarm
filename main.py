
import alarm_puzzle

if __name__ == '__main__':
    ap = alarm_puzzle.alarm_puzzle()
    # ap.push_button(4)
    # ap.push_button(1)
    # ap.push_button(2)
    # ap.push_button(3)

    arr = [5, 2, 9, 2]
    n = 4
    Ans = ap.largest(n)
    info = 1
    print("Largest in given array is", Ans)
    n = 3

    Ans = ap.largest(n)
    info = 2
    print("second Largest in given array is", Ans)
    n = 2

    Ans = ap.largest(n)
    info = 3
    print("third Largest in given array is", Ans)

    n = 1
    Ans = ap.largest(n)
    info = 4
    print("fourth Largest in given array is", Ans)
    print(ap.solved)



"""
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

