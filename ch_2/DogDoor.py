from time import sleep
from bark import Bark

class DogDoor(object):
	"""docstring for DogDoor"""
	def __init__(self):
		self.open = open
		self.allowedBark = Bark('')

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

	def setAllowedBark(self, sound):
		self.allowedBark = Bark(sound)
	
	def getAllowedBark(self):
		return self.allowedBark

door = DogDoor()
door.setAllowedBark("Woa")
print(type(door.getAllowedBark()))
