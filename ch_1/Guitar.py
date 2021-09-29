#from FindGuitarTester import Builder, Type, Wood
class GuitarSpace:
	def __init__(self,builder,type_of, model,backwood, topwood, num_strings):
		self.type_of, self.builder, self.model,self.backwood, self.topwood, self.num_strings = type_of, builder, model,backwood, topwood,num_strings

	def get_builder(self):
		return self.builder

	def get_model(self):
		return self.model
	
	def get_type(self):
		return self.type_of

	def get_backwood(self):
		return self.backwood

	def get_num_strings(self):
		return self.num_strings


class Guitar:
	"""docstring for ClassName"""
	def __init__(self, serialnumber, price, builder,type_of, model,backwood, topwood,num_strings=12):
		self.serialnumber, self.price, self.spec = serialnumber, price, GuitarSpace(builder,type_of, model,backwood, topwood, num_strings)

	## gettters
	def get_serialnumber(self):
		return self.serialnumber

	def get_price(self):
		return self.price

	def get_spec(self):
		return self.spec

	## Setters
	def set_backwood(self , price):
		self.price = price

#new_guitar = Guitar("",0,Builder.FENDER, "Sratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER)
#print(new_guitar.get_type())