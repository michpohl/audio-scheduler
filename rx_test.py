from rx import Observable, Observer
from rx.subjects import Subject
import RPi.GPIO as GPIO
import time
from led_controller import Blinker
 
SENSOR_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)


# source = Observable.create(say_something)

# class Whatever():
	

		
class MyObserver(Observer):

	def subscribe_to_stream(self, y):
		d = y.subscribe(lambda x: print("Got: %s" % x))
		
		def on_next(self):
			print ("on_next!")
		
		def on_error(self):
			pass
		
		def on_completed(self):
			pass 
			
			
# a = Whatever()
# b = MyObserver()

# b.subscribe_to_stream(a.stream)
# a.test()

# mySource = MyObservable()	
# mySource.source.subscribe(PrintObserver())



streamyStream = Observable.create(lambda observer: GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=lambda p: observer.on_next(p), bouncetime=50)

streamyStream().subscribe(MyObserver())
