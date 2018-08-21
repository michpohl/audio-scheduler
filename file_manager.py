import random
from os import listdir
from os.path import isfile, join

class FileManager:

	def __init__(self):
		pass
		
	def get_files_in_path ( self, str ):
		onlyfiles = [f for f in listdir(str) if isfile(join(str, f))]
		return onlyfiles

	def print_list_elements ( self, list ):
		for element in list: print (element)
		return
		
	def random_element ( self, list ):
		return random.choice(list)	

	