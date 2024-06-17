from DogDoor import DogDoor
from Remote import Remote
from BarkRecognizer import BarkRecognizer
from bark import Bark


class DogDoorSimulate(object):
    def __init__(self):
        self.door = DogDoor()
        self.rec = BarkRecognizer(self.door)
        # self.remote = Remote(self.door)

    def main(self):
        barks = [Bark("Bark" + str(i)) for i in range(3)]
        self.door.setAllowedBark(barks)
        print("Allowed Barks :> ", self.door.getAllowedBark())
        print("Bruce starts barking")
        # call bark recognizer to recognize the sound
        self.rec.recognize(Bark("Bark1"))


test = DogDoorSimulate()
test.main()

"""
To do :
1  specify our dog barks
2  Simulate hardware hearing another bark
3  if our dof get stuck outside
"""
