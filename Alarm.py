class Alarm:
    alarm_time = None
    subscribers = []
    disarmed = False
    willRing = False

    def __init__(self, date_time_alarm, willRing=False):
        self.alarm_time = date_time_alarm
        self.willRing = willRing

    def set_will_ring(self, will_ring):
        self.willRing = will_ring

    def subscribe(self, observer):
        self.subscribers.append(observer)

    def unsubscribe(self, observer):
        self.subscribers.remove(observer)

    def is_disarmed(self):
        return self.disarmed

    def set_disarmed(self, disarmed):
        self.disarmed = disarmed

    def notify(self, time):
        if self.willRing and time.time_is(self.alarm_time):
            print("Alarm time!")
            for observer in self.subscribers:
                observer.notify(self)
