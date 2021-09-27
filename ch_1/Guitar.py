
class Guitar:
	"""docstring for ClassName"""
	def __init__(self, serialnumber, price, builder,type_of, model,backwood, topwood):
		self.serialnumber, self.price, self.type_of, self.builder, self.model,backwood, self.topwood = serialnumber , price, type_of, builder, model,backwood, topwood

	## gettters
	def get_serialnumber(self):
		return self.serialnumber

	def get_price(self):
		return self.price

	def get_builder(self):
		return sel.builder

	def get_model(self):
		return self.model
	
	def get_typ(self):
		return self.type_of

	def get_backwood(self):
		return self.model
	## Setters
	def set_price(self , price):
		self.price = price




class FindGuitarTester:
	def __init__(self, **kwargs):

		inventory = Inventory()
		initializeInventory(inventory)
		new = Guitar(**kwargs)