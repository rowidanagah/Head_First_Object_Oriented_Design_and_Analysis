from instrument import Instrument
from InstrumentSpec import *

class Inventory(object):
	"""docstring for Inventory"""
	def __init__(self):
		self.lst = []

	def addInstrument(self,ins):
		## arg would be an Instrumentspace or Instrument obj
		self.lst.append(ins)

	def getInstrument(self, srl_num):
		for ins in self.lst:
			if ins.srl_num == srl_num:
				return ins
		return None

	def search(self, searchSpace):
		ans = [] # for more than one match
		for ins in self.lst:
			if searchSpace.match(ins.getSpace()):
				print("Here" , ans)
				ans.append(ins)
		return ans

