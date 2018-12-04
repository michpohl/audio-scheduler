import RPi.GPIO as GPIO
import time
from led_controller import Blinker

SENSOR_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)


class MotionDetector:

    def __init__(self, callback_method):
        self.callback_method = callback_method
        self.sleep_time = 1
        blinker = Blinker()

    def set_sleep_time(self, counter):
        print ("setting sleep time to: " + str(counter))
        self.sleep_time = counter
        print (self.sleep_time)

    def get_sleep_time(self):
        return self.sleep_time

    def detect(self):

        try:
            callback = lambda x, arg1=self.get_sleep_time(): self.callback_method(arg1)
            GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, self.callback_method)

        except KeyboardInterrupt:
            print ("Beende...")
            GPIO.cleanup()
