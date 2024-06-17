from instrument import Instrument
from InstrumentSpec import *
from Guitar import *
from Mandolin import MandolinSpec, Mandolin


class Inventory(object):
    """docstring for Inventory"""

    def __init__(self):
        self.lst = []

    def addInstrument(self, serialNumber, price, spec):
        ## arg would be an InstrumentSpace or Instrument obj
        ins: Instrument = None
        if isinstance(spec, GuitarSpec):
            ins = Guitar(serialNumber, price, spec)
        if isinstance(spec, MandolinSpec):
            ins = Mandolin(serialNumber, price, spec)
        if ins:
            self.lst.append(ins)
            return

    def getInstrument(self, srl_num):
        for ins in self.lst:
            if ins.srl_num == srl_num:
                return ins
        return None

    def search(self, searchIns: Instrument):
        ans = []  # for more than one match
        for ins in self.lst:
            if searchIns.getSpace().match(ins.getSpace()):
                print("Here", ans)
                ans.append(ins)
        return ans


sd = MandolinSpec("builder", "type_of", "model", "backwood", "topwood", Style.STYLE1)

s = MandolinSpec("builder", "type_of", "model", "backwood", "topwood", Style.STYLE1)


s = GuitarSpec("builder", "type_of", "model", "backwood", "topwood", "numStrings")
