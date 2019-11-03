from gpiozero import OutputDevice
from threading import Thread
import time

class Buzzer:

    speaker = OutputDevice(13)
    sound = True
    t = None

    def __init__(self):
        self.t = Thread(target=self.run)

    def run(self):
        while self.sound:
            self.speaker.toggle()
            time.sleep(1/660)


    def start(self):
        self.t.start()

    def stop(self):
        self.sound = False


