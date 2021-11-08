
from DogDoor import DogDoor

class BarkRecognizer(object):
	"""docstring for BarkRecognizer"""
	def __init__(self, door):
		self.door = door
		
	def recoginzer(self , bark ):

		# For now it's any random bark will work for us
		print("BarkRecognizer  heared a " , bark ) 
		self.door.Open()