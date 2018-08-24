import time
from motion_detector import MotionDetector
from led_controller import Blinker
from queue import Queue
from threading import Thread
from audio_controller import Player
from file_manager import FileManager
from random import randint


# global stuff unfortunately
def detector_callback(self):
			global blinker
			blinker.multiple_blink(2)
			print("Motion detected!")
			global pause
			print ("subtracting from pause")
			if pause > 15:
				pause -= 4
			else: 
				pause = pause -1
			if (pause < 1):
				pause = 1
			print ("new pause: " + str(pause))
			global detection_timestamp
			detection_timestamp = time.time()
			print (" time stamp: " + str(detection_timestamp))
pause = 1
detection_timestamp = 0
detector = MotionDetector(detector_callback)
queue = Queue()
blinker = Blinker()


class EventManager():
		
	file_folders = ["a","b","c","d"]
	file_manager = FileManager()
		
	def start(self):
			
			global detection_timestamp
			detection_timestamp = time.time()
			global queue
			player_threads = []
			
			for folder in self.file_folders:
				print ("Adding a thread to the player threads at index: " + str(self.file_folders.index(folder)))
				player_threads.append(Thread( target=self.player_thread, args=(queue, self.file_folders.index(folder))))
			
			detect_thread = Thread( target=self.detection_thread, args=("Thread: motion detector", queue) )
	
			for thread in player_threads:
				thread.start()
				time.sleep(2)
		
			detect_thread.start()
			while True:
				self.handle_queue()
			for thread in player_threads:
				thread.join()			
			detect_thread.join()	
	
	def handle_queue(self):
		global queue
		# print ("handling")
		self.adjust_pause()
		queue.put(1)
		time.sleep(0.5)
	
	def adjust_pause(self):
		global pause
		global detection_timestamp
		print ("silence since last motion: " + str(time.time() - detection_timestamp))
		if (time.time() - detection_timestamp > 10):
			if (pause <= 30):
				pause += 2
				print ("new pause: " + str(pause))
			detection_timestamp = time.time()
		
	
	def player_thread(self, queue, audio_channel):
		files_for_player = self.file_manager.get_files_in_path(self.file_folders[audio_channel])
		player = Player(self.file_folders[audio_channel], audio_channel)
				
		while True:
			global pause
			if pause is None: return
			print ("player thread on channel: " + str(audio_channel) + " plays")
			print ("player_thread on channel: " + str(audio_channel) + " sleeps for: " + str(pause))
			# player.play(channel = audio_channel)
			player.play_random()
			time.sleep(pause)
	
	def detection_thread(self, threadname, q):
	
		
		global detector
		detector.detect()
		print("do we get here?")
		time.sleep(0.1)

