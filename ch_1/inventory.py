

class Inventory:
	def __init__(slef):
		self.guitars_lst = []

	def add_guitar(self,serialnumber, price, builder,type_of, model,backwood, topwood):
		guitar = Guitar(serialnumber, price, builder,type_of, model,backwood, topwood)
		self.guitars_lst.append(guitar)

	def display_guitar(self, gtrs_list):
		for i in range(len(gtrs_list)):
			print("Guitar :", i+1)
			print("serial number:", guitars_lst[i].serialnumber)
			print("builder version = ", guitars_lst[i].builder)
			print("type = ", guitars_lst[i].type_of)
			print("backwood = ", guitars_lst[i].backwood)
			print("topWood = ", guitars_lst[i].topwood)
			print("price = ", guitars_lst[i].price)
			##print("num of strings = ", guitars_lst[i].guitar_spec.num_strings)

	def get_guitar(self, serialnumber):
		for guitar in self.guitars:
			if guitar.serialnumber == serialnumber:
				return guitar.price
		return None

	def search_guitar(msg):
		"""
		A decorator with args
		"""
		def inner_func(**kwargs):
			"""
			Ignore serial number since it's unique
			Ignore serial number price it's unique
			"""
			for guitar in self.guitars:
				if any( builder != self.builder and 
					type_of != self.type_of and model != self.model and 
					topwood != self.topwood and backwood != self.backwood
					):
					return None
				else :
					guitar = Guitar(**kwargs)
					return guitar

		return inner_func
