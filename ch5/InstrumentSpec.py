from enum import Enum
class Type(Enum):
	"""
	This class is created to get rid of and ditch this annoying string comparssion.
	"""
	COUSTIC = "ACOUSTIC"
	ELECTRIC = "ELECTRIC"

	def to_string(self):
		return ACOUSTIC.Title() , ELECTRIC.Title()

	def __repr__(self):
		return "{} or {}".format(ACOUSTIC.Title() , ELECTRIC.Title())


class Builder(Enum):
    FENDER = "FENDER"
    MARTIN = "MARTIN"
    GIBSON = "GIBSON"

    def to_string(self):
    	return FENDER.Title, GIBSON.Title(), MARTIN.Title()

    def __repr__(self):
    	return "{}, {}, or {}".format(FENDER.Title, GIBSON.Title(), MARTIN.Title())

class Wood(Enum):
	CEDAR = "CEDAR"
	MAPLE = "MAPLE"
	COCOBOLO = "COCOBOLO"
	ALDER = "ALDER"

	def to_string(self):
		return CEDAR.Title() , ALDER.Title() , COCOBOLO.Title(), MAPLE.Title() 

	def __repr__(self):
		return "{}, {}, {}, or {}".format(CEDAR.Title() , ALDER.Title() , COCOBOLO.Title(), MAPLE.Title())


class InstrumentSpec:
	def __init__(self):

	def getBuilder(self):
		return self.builder

	def getModel(self):
		return self.model
	
	def getType(self):
		return self.type_of

	def getBackwood(self):
		return self.backwood
	
	def getTopwood(self):
		return self.backwood
