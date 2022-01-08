class Tile(object):
	"""docstring for Tile"""
	def __init__(self):
		self.units = []
		
	def addUnit(self, unit):
		self.units.append(unit)

	def removeUnit(self,unit):
		self.units.remove(unit)
