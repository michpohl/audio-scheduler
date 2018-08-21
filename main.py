from led_controller import Blinker
from audio_controller import Player
from motion_detector import MotionDetector

from queue import Queue
from threading import Thread
from functools import partial
from event_manager import EventManager

from rx import Observable, Observer
from rx.subjects import Subject

import random
import time

# strg shift hoch und runter
# srg q

blinker = Blinker()
# player = Player()
manager = EventManager()

filefolder = "folder"
interval = 1



def get_files_in_path ( str ):
	onlyfiles = [f for f in listdir(str) if isfile(join(str, f))]
	return onlyfiles

def print_list_elements ( list ):
	for element in list: print (element)
	return
	
def random_element ( list ):
	return random.choice(list)



def start_multi_channel_audio(interval, folders):
		threads = [Thread, Thread, Thread, Thread]
		for folder in folders:
				channel_index = folders.index(folder)
				print("current thread number:"  +  str(channel_index))
				print("current folder:" + folder)
				files = get_files_in_path(folder)
				threads[channel_index] = Thread(target = player.play_with_interval, args =(interval, folder, files, channel_index))
				threads[channel_index].start()

				
def start_motion_detection():
	global interval
	detector = MotionDetector(detector_callback)
	detection_thread = Thread(target = trigger_detector(detector))
	detection_thread.start()
	
def trigger_detector(detector):
	detector.detect()
	
def detector_callback(callback_channel):
	blinker.multiple_blink(2)
	print("Motion detected!")
	adjust_playback_interval(main_queue)
	
	   
def adjust_playback_interval(queue):
	interval = player.interval
	print("The interval is " + str(interval))
	interval = interval + 1
	print("Adding 1. The interval is now " + str(interval))
	queue.put(interval)


manager.start()


