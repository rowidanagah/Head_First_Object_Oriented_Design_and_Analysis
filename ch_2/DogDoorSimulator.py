from DogDoor import DogDoor
from Remote import Remote
from BarkRecognizer import BarkRecognizer

class DogDoorSimulate(object):
	"""docstring for DogDoorSimulate"""
	def __init__(self):
		self.door = DogDoor()
		self.rec = BarkRecognizer(self.door)
		# self.remote = Remote(self.door) 


	def main(self):
		print("Fido barks to go out side")
		self.rec.recoginzer("WHO WHOAA")
		
		##self.remote.pressButton()

		print(self.door.open)
		print("Fido barks to go outside")
		print("Fido has gone outside")
		print("Fido's all done ... ")
		print("Fido's  back inside ")

test_drive = DogDoorSimulate()
test_drive.main()
"""

To do :
	1 - specify our dog barks
	2 - Simulate hardware hearing another bark
	3 - if our dof get stuck outside

"""