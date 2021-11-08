
from time import sleep

class DogDoor(object):
	"""docstring for DogDoor"""
	def __init__(self):
		self.open = open

	def isOpen(self):
		return self.open

	def Open(self):
		print("The dog door opens")
		self.open = True
		# Thread wait for a 5 secs and then Close!
		sleep(5)
		self.Close()

	def Close(self):
		print("The dog door closes")
		self.open = False

