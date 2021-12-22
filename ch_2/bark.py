class Bark:
	def __init__(self , sound):
		self.sound = sound
	def getSound(self):
		return self.sound
	def equal(self,another_bark):
		if isinstance(another_bark, Bark):
			return self.sound == another_bark.sound
		else :
			return False

obj = Bark("Woa!")
obj2 = Bark("Whhoa!")
obj1 = Bark("Woa!")

"""
print(obj.equal(obj2))
print(obj.equal(obj1))
"""