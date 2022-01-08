from Tile import Tile
class Board(object):
	"""docstring for Board"""
	
	def __init__(self, width, hight):
		self.width = width
		self.hight = hight
		self.tiles =[]
		self.initialize()

	def initialize(self):
		"""
		We will present the grid of the board as an W*H array of arrays
		"""
		self.tiles = [[Tile() for _ in range(self.width)] for j in range(self.hight)]

	def getTile(self, x, y):
		return self.tiles[x-1][y-1]

	def addUnit(self, unit, x, y):
		tile = self.getTile(x, y)
		tile.addUnit(unit)

	def removeUnit(self, unit, x, y):
		tile = self.getTile(x, y)
		tile.removeUnit()

	def getUnit(self, x, y):
		tile = self.getTile(x, y)
		return tile.getUnit()

brd = Board(2,2)
print(brd.tiles)
