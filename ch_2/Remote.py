from DogDoor import DogDoor
from time import sleep


class Remote:
	"""
	This class is used to allow a remote controll to operate the dog door.
	Without getting out of home
	"""
	def __init__(self, door):
		self.door = door

	def pressButton(self):
		"""
		To keep ut withwhether the door is opened or not
		"""
		if (self.door.isOpen()):
			self.door.Close()
		else :
			self.door.Open()
			

"""
dorr = DogDoor()
r = Remote(dorr)
r.pressButton()
"""

