import os
from os.path import isfile, join
import random
import time
from pygame import mixer
from multiprocessing import Process
import sounddevice as sd
import soundfile as sf
from file_manager import FileManager


class Player:

	channels = ["stereo1", "stereo2", "stereo3", "stereo4"]
	keep_playing = True
	interval = 0
	file_manager = FileManager()
	
	def __init__(self, folder, channel):
		self.folder = folder
		print ("Folder is: " + folder)
		self.files = self.file_manager.get_files_in_path(folder)
		self.channel = self.channels[channel]
		print ("initializeing player...")
		print ("...on channel: " + str(channel))
		# self.mixer = mixer
		# mixer.init()
		print (str(sd.query_devices()))
		sd.default_device = channel
		sd.default.samplerate = 44100
		
    
	def play(self):
		print ("player plays on channel " + str(self.channel))
		os.system("aplay /home/pi/2.wav -D " + self.channel)
		# self.mixer.music.load("/home/pi/2.wav")
		# self.mixer.music.play()
		# data, fs = sf.read("/home/pi/2.wav")
		# sd.play(data, fs, blocking = True)
		# sd.wait()
		
	def play_random(self):
		file_to_play = random.choice(self.files)
		print ("playing file:"  + file_to_play + " on channel: ", self.channel)
		os.system("aplay " + self.folder + "/" + file_to_play + " -D " + self.channel)
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