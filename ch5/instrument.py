class Instrument(object):
    """
    docstring for Instrument
    """

    def __init__(self, srl_num, price, spec):
        self.InstrumentSpace = spec
        self.price = price
        self.srl_num = srl_num

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def getsrl_num(self):
        return self.srl_num

    def getSpace(self):
        return self.InstrumentSpace

    def __str__(self) -> str:
        return "Instrument is "
