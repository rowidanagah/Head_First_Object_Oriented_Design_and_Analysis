class DogDoor(object):
	"""docstring for DogDoor"""
	def __init__(self):
		self.open = open

	def isOpen(self):
		return self.open

	def Open(self):
		print("The dog door opens")
		self.open = True

	def Close(self):
		print("The dog door closes")
		self.open = False

