class Tile(object):
	"""docstring for Tile"""
	def __init__(self):
		self.units = []
		
	def addUnit(self, unit):
		self.units.append(unit)

	def getUnit(self):
		return self.units

	def removeUnit(self,unit):
		self.units.remove(unit)

	def removeUnits(self):
		self.units.clear()
