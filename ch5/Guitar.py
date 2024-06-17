from InstrumentSpec import *
from instrument import *


class GuitarSpec(InstrumentSpec):
    def __init__(self, builder, type_of, model, backwood, topwood, numStrings):
        super().__init__(builder, type_of, model, backwood, topwood)
        self.numStrings = numStrings

    def getNumStrings(self):
        return self.numStrings

    def match(self, InsSpec):
        if super().match(InsSpec):
            return (
                isinstance(InsSpec, GuitarSpec)
                and InsSpec.numStrings == self.numStrings
            )
        return False


class Guitar(Instrument):
    def __init__(self, serialNumber, price, spec: GuitarSpec):
        super().__init__(serialNumber, price, spec)

    def __str__(self) -> str:
        return super().__str__() + "Guitar"


s = GuitarSpec("builder", "type_of", "model", "backwood", "topwood", "numStrings")
s2 = GuitarSpec("builder", "type_of", "model", "backwood", "topwood", "numStrings")
print(s.match(s2))

gt = Guitar("ser", 32, s)
print(gt)
