from time import sleep
from bark import Bark


class DogDoor(object):
    """docstring for DogDoor"""

    def __init__(self):
        self.isOpen = False
        self.allowedBark = []  # Bark('')

    def isOpen(self):
        return self.open

    def open(self):
        print("The dog door opens")
        self.isOpen = True
        # Thread wait for a 5 secs and then Close!
        sleep(5)
        self.close()

    def close(self):
        print("The dog door closes")
        self.isOpen = False

    def setAllowedBark(self, sound):
        self.allowedBark = [brk for brk in sound]

    def getAllowedBark(self):
        return [brk for brk in self.allowedBark] if self.allowedBark else "None"


"""
door = DogDoor()
door.setAllowedBark("Woa")
print(type(door.getAllowedBark()))
"""
