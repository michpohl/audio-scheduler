import os
from os.path import isfile, join
import random
import time
from pygame import mixer
from multiprocessing import Process
import sounddevice as sd


class Player:

	channels = ["stereo1", "stereo2", "stereo3", "stereo4"]
	keep_playing = True
	interval = 0
	
	# def __init__(self):
		# interval = 1
		# self.mixer = mixer
		# mixer.init()
		# self.files = files
		# sd.query_devices()
		
    
	def play(self, channel):
		print ("player plays")
		os.system("aplay /home/pi/2.wav -D " + self.channels[channel])
		# self.mixer.music.load("/home/pi/2.wav")
		# self.mixer.music.play()
		
	# def play_random(self):
		# file_to_play = random.choice(self.files)
		# print ("playing file:"  + file_to_play + " on channel: ", self.channel)
		# self.mixer.music.load(file_to_play)
		# self.mixer.music.play(channels[self.channel])
		
	def play_with_interval(self, interval, folder, files, channel_index):
		channel = self.channels[channel_index]
		print (channel_index)
		print("starting playback on channel ", channel)
		print (folder)
		while True:
			try:
				file_to_play = random.choice(files)
				self.play_files_in_folder(folder, file_to_play, channel)
				self.keep_playing = False
				time.sleep(interval)
			except KeyBoardInterrupt:
				return

	def set_interval(self, value):
		if (interval > value):
			print ("Slowing down the interval: " + str(inteval) + " to " + str(value))
		if (interval < value):
			print ("Speeding up the interval " + str(inteval) + " to " + str(value))	
		interval = value