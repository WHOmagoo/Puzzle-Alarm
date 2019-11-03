class Alarm:
    alarm_time = None
    subscribers = []
    disarmed = False



    def __init__(self, date_time_alarm):
        self.alarm_time = date_time_alarm


    def subscribe(self, observer):
        self.subscribers.append(observer)

    def unsubscribe(self, observer):
        self.subscribers.remove(observer)

    def is_disarmed(self):
        return self.disarmed

    def set_disarmed(self, disarmed):
        self.disarmed = disarmed

    def notify(self, time):
        if time.time_is(self.alarm_time):
            for observer in self.subscribers:
                observer.notify(self)
