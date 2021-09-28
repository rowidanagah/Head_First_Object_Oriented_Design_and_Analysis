#from FindGuitarTester import Builder, Type, Wood

class Guitar:
	"""docstring for ClassName"""
	def __init__(self, serialnumber, price, builder,type_of, model,backwood, topwood):
		self.serialnumber, self.price, self.type_of, self.builder, self.model,self.backwood, self.topwood = serialnumber , price, type_of, builder, model,backwood, topwood

	## gettters
	def get_serialnumber(self):
		return self.serialnumber

	def get_price(self):
		return self.price

	def get_builder(self):
		return self.builder

	def get_model(self):
		return self.model
	
	def get_type(self):
		return self.type_of

	def get_backwood(self):
		return self.model
	## Setters
	def set_price(self , price):
		self.price = price

#new_guitar = Guitar("",0,Builder.FENDER, "Sratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
#print(new_guitar.get_type())