from DogDoor import DogDoor
from bark import Bark


class BarkRecognizer(object):
    """docstring for BarkRecognizer"""

    def __init__(self, door):
        self.door = door

    def recognize(self, bark: Bark):  # Bark obj
        # For now, any random bark will work for us
        print("BarkRecognizer  heard a ", bark)
        print([brk for brk in self.door.allowedBark])
        for brk in self.door.allowedBark:
            print(bark.equal(brk), brk, self.door)
            if bark.equal(brk):
                print("open the door")
                self.door.open()
                return
        return "this barking, it's not allowed here!"


dog = DogDoor()
rec = BarkRecognizer(dog)
