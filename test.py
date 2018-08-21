import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

class Blinker:
	
	def blink(self):
		counter = 9
		while counter >0:
			print "LED on"
			GPIO.output(17,GPIO.HIGH)
			time.sleep(0.1)
			print "LED off"
			GPIO.output(17,GPIO.LOW)
			time.sleep(0.2)
			counter -= 1
			print counter
		
x = Blinker()
x.blink()
