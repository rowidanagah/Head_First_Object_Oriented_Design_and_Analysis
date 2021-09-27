from enum import Enum

class Type(Enum):
	"""
	This class is created to get rid of this annoying string comparssion.
	"""
	COUSTIC = "ACOUSTIC"
	ELECTRIC = "ELECTRIC"

	def to_string(self):
		return ACOUSTIC.Title() , ELECTRIC.Title()


class Builder(Enum):
    FENDER = "FENDER"
    MARTIN = "MARTIN"
    GIBSON = "GIBSON"

    def to_string(self):
    	return FENDER.Title, GIBSON.Title(), MARTIN.Title()

class Wood(Enum):
	CEDAR = "CEDAR"
	MAPLE = "MAPLE"
	COCOBOLO = "COCOBOLO"
	ALDER = "ALDER"

	def to_string(self):
		return CEDAR.Title() , ALDER.Title() , COCOBOLO.Title(), MAPLE.Title() 


class FindGuitarTester:
	def __init__(self, **kwargs):

		inventory = Inventory()
		initializeInventory(inventory)
		new = Guitar(**kwargs)