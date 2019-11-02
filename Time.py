import datetime
from threading import Thread

class Time:
    cur_time = 0
    monitor_thread = None


    toNotify = []

    def __init__(self):
        self.cur_time = datetime.datetime.now()
        self.monitor_thread = Thread(target=self.subscribe_to_time_change)
        self.monitor_thread.start()

    def get_time(self):
        return self.cur_time

    def subscribe_to_time_change(self, toNotify):
        self.toNotify.append(toNotify)

    def monitor_time(self):
        while True:
            new_time = datetime.datetime.now()
            if self.cur_time.time.minute != new_time.time.minute:
                self.cur_time = new_time
                for item in self.toNotify:
                    item.notify(self)





