from DogDoor import DogDoor
from time import sleep


class Remote:
    """
    This class is used to allow a remote controller to operate the dog door.
    Without getting out of home
    """

    def __init__(self, door):
        self.door = door

    def pressButton(self):
        """
        To keep it withwhether the door is opened or not
        """
        if self.door.isOpen():
            self.door.close()
        else:
            self.door.open()


"""
dorr = DogDoor()
r = Remote(dorr)
r.pressButton()
"""
