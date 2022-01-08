from Inventory import Inventory
from InstrumentSpec import *
from instrument import Instrument

class FindGuitarTester(object):
	"""docstring for FindGuitarTester"""
	def __init__(self):
		self.inv = Inventory()
		self.initializeInv()
	
	def main(self):
		Spec = {"model":"abc"}
		Spec2 =  {"builder" :Builder.FENDER}
		insSpec = InstrumentSpec(Spec2)
		ans = self.inv.search(insSpec) ## We will search with insSpec cllass properties

	def initializeInv(self):
		specs1 = {"instrument":InstrumentType.GUITAR,"strings":12,"builder":Builder.FENDER, "type":Type.ELECTRIC, "model":"Sratocastor","back_wood":Wood.ALDER,"top_wood":Wood.ALDER }
    	instrument1 = Instrument("1", 1499.95, specs1)
    	specs2 = {"instrument":InstrumentType.GUITAR,"strings":12,"builder":Builder.FENDER, "type":Type.ELECTRIC, "model":"Sratocastor","back_wood":Wood.ALDER,"top_wood":Wood.ALDER }
    	instrument2 = Instrument("1", 1499.95, specs1)
    	
    	specs3 = {"instrbument":InstrumentType.MANDOLIN,"strings":12,"builder":Builder.FENDER, "type":Type.ELECTRIC, "model":"Sratocastor","back_wood":Wood.ALDER,"top_wood":Wood.ALDER }
    	instrument3 = Instrument("1", 1499.95, specs1)
    	
    	specs4 = {"instrument":InstrumentType.BANJO,"strings":12,"builder":Builder.FENDER, "type":Type.ELECTRIC, "model":"Sratocastor","back_wood":Wood.ALDER,"top_wood":Wood.ALDER }
    	instrument4 = Instrument("1", 1499.95, specs1)


		self.inv.addInstrument(instrument1)
		self.inv.addInstrument(instrument2)
		self.inv.addInstrument(instrument3)
		self.inv.addInstrument(instrument4)


obj = FindGuitarTester()
print(obj.main())