import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)

class Blinker:
	
	def blink(self):
		print ("LED on")
		GPIO.output(17,GPIO.HIGH)
		time.sleep(0.1)
		print ("LED off")
		GPIO.output(17,GPIO.LOW)
		
	def multiple_blink(self, number):
		counter = number
		print ("Blinking " + str(counter) +  " times.")
		while counter >0:
			GPIO.output(17,GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(17,GPIO.LOW)
			time.sleep(0.1)
			counter -= 1
