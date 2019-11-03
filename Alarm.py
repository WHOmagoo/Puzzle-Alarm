class Alarm:
    alarm_time = None
    subscribers = []



    def __init__(self, date_time_alarm):
        self.alarm_time = date_time_alarm


    def subscribe(self, observer):
        self.subscribers.append(observer)

    def unsubscribe(self, observer):
        self.subscribers.remove(observer)

    def notify(self, time):
        if time.time_is(self.alarm_time):
            for observer in self.subscribers:
                observer.notify(self)
