import time

import Alarm
import Time
import AlarmActions
import datetime

import TimeToArray
import AlarmPuzzle
import SevenSegDriver

import Buttons

if __name__ == '__main__':
    Buttons.Buttons()



    # cur_time.subscribe_to_time_change()
    # alarm_time = cur_time.get_time()

    # alarm_time = datetime.datetime(alarm_time.year, alarm_time.month, alarm_time.day, alarm_time.hour, alarm_time.minute + 1, alarm_time.second)

    # alarm = Alarm.Alarm(alarm_time)

    # cur_time.subscribe_to_time_change(alarm)

    # alarmResult = AlarmActions.AlarmActions()

    # alarm.subscribe(alarmResult)

    # while not alarm.disarmed:
    #     print("waiting", cur_time.get_time().second)
    #     time.sleep(5)
