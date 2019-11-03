from gpiozero import Button

import SevenSegDriver
import Time
import TimeToArray
import Alarm
import alarm_puzzle
import datetime
import AlarmActions

class Buttons:
    # button 4
    button4 = Button(14)

    # button 3
    button3 = Button(15)

    # button 2
    button2 = Button(18)

    # button 1
    button1 = Button(23)

    mode = "view"

    alarm = None

    prev_pushed = -1
    screen = None

    alarm_puzzle = None

    def __init__(self):
        cur_time = Time.Time()

        self.screen = SevenSegDriver.SevenSegDrive(TimeToArray.time_to_array(cur_time.get_time()))

        cur_time.subscribe_to_time_change(self.screen)

        cur_time_e = cur_time.get_time().time()
        alarm_time = datetime.time(cur_time_e.hour, cur_time_e.minute + 1, 0)

        print("Alarm for ", alarm_time)

        self.alarm = Alarm.Alarm(alarm_time)
        self.alarm.willRing = True

        self.alarm_puzzle = alarm_puzzle.alarm_puzzle()

        self.alarm.subscribe(self)

        cur_time.subscribe_to_time_change(self.alarm)

        self.mode = "view"


    def notify(self, alarm):
        print("mode is alarm now")
        self.mode = "alarm"
        self.screen.set_mode("alarm", self.alarm_puzzle)


    def poll_buttons(self):
        if self.mode is "alarm":
            self.screen.mode("alarm", alarm_puzzle)

            if self.button1.is_active and self.prev_pushed != 1:
                self.alarm_puzzle.push_button(1)
                self.prev_pushed = 1
            elif self.button2.is_active and self.prev_pushed != 2:
                self.alarm_puzzle.push_button(2)
                self.prev_pushed = 2
            elif self.button3.is_active and self.prev_pushed != 3:
                self.alarm_puzzle.push_button(3)
                self.prev_pushed = 3
            elif self.button4.is_active and self.prev_pushed != 4:
                self.alarm_puzzle.push_button(4)
                self.prev_pushed = 4
            else:
                self.prev_pushed = -1

            if self.alarm_puzzle.is_solved():
                self.mode = "view"
                self.screen.mode("view")


        if self.mode is "view":
            if not (self.button1.is_active and self.button2.is_active):
                if self.button1.is_active:
                    self.mode = "change_time"

                if self.button2.is_active:
                    self.mode = "change_alarm"





