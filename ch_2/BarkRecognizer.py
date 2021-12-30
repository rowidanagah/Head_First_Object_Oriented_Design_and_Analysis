from DogDoor import DogDoor

class BarkRecognizer(object):
	"""docstring for BarkRecognizer"""
	def __init__(self, door):
		self.door = door
		
	def recoginzer(self , bark ): # Bark obj
		# For now, any random bark will work for us
		print("BarkRecognizer  heared a " , bark ) 
		print([brk for brk in self.door.allowedBark])
		for brk in self.door.allowedBark:
			if brk.equal(bark):
				print("open the door")
				self.door.open();
				return
		return "this barking, it's not allowed here!"

dog = DogDoor()
rec = BarkRecognizer(dog)

