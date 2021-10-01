from DogDoor import DogDoor
from Remote import Remote


class DogDoorSimulate(object):
	"""docstring for DogDoorSimulate"""
	def __init__(self):
		self.door = DogDoor()
		self.remote = Remote(self.door)


	def main(self):
		print("Fido barks to go out side")
		self.remote.pressButton()
		print(self.door.open)
		print("Fido barks to go outside")
		self.remote.pressButton()
		print("Fido has gone outside")
		self.remote.pressButton()
		print("Fido's all done ... ")
		self.remote.pressButton()
		print("Fido's  back inside ")
		self.remote.pressButton()

test_drive = DogDoorSimulate()
test_drive.main()
