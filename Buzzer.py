from gpiozero import OutputDevice
from threading import Thread
import time

class Buzzer:

    speaker = OutputDevice(13)
    sound = True
    t = None
    buzzing = False

    def __init__(self):
        self.t = Thread(target=self.run)

    def run(self):
        self.buzzing = True
        print("Starting sound")
        self.speaker.on()
        while self.buzzing:
            self.speaker.toggle()
            time.sleep(1/660)
        print("Stopping sound")
        self.speaker.off()
        self.buzzing = False

    def start(self):
        if not self.buzzing:
            self.t.start()

    def stop(self):
        if self.buzzing:
            self.buzzing = False
            print("Stopped sound")
            self.t = Thread(target=self.run)


