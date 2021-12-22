from DogDoor import DogDoor

class BarkRecognizer(object):
	"""docstring for BarkRecognizer"""
	def __init__(self, door):
		self.door = door
		
	def recoginzer(self , bark ): # Bark obj
		# For now, any random bark will work for us
		print("BarkRecognizer  heared a " , bark ) 
		lst = door.getAllowedBark();
		for brk in lst:
			if brk.equal(bark):
				self.door.open();
				return
		return "this barking, it's not allowed here!"