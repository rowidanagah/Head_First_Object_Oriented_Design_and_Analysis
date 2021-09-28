from guitar import Guitar

class Inventory:
	def __init__(self):
		self.guitars_lst = []

	def add_guitar(self , new_guitar):#:,serialnumber, price, builder,type_of, model,backwood, topwood):
		#new_guitar = Guitar(serialnumber, price, builder,type_of, model,backwood, topwood)
		self.guitars_lst.append(new_guitar)

	def display_guitar(self, gtrs_list = []):
		if not gtrs_list:
			"""
			in ase of we need to displa the whole guitars that we have
			"""
			gtrs_list = self.guitars_lst

		for i in range(len(gtrs_list)):
			print("Guitar :", i+1)
			print("serial number:", gtrs_list[i].serialnumber)
			print("builder version = ", gtrs_list[i].builder)
			print("type = ", gtrs_list[i].type_of)
			print("backwood = ", gtrs_list[i].backwood)
			print("topWood = ", gtrs_list[i].topwood)
			print("price = ", gtrs_list[i].price)
			##print("num of strings = ", gtrs_list[i].guitar_spec.num_strings)

	def get_guitar(self, serialnumber):
		for gt in self.guitars_lst:
			"""
			we would search by serialnumber as it's unique
			"""
			if gt.serialnumber == serialnumber:
				return gt.price
		return None

	def search_guitar(self, customer_gt):
		"""
			Ignore serial number since it's unique
			Ignore price number price it's unique
		"""
		guitars_found = []
		for gt in self.guitars_lst:
			if self.match(gt , customer_gt):
				guitars_found.append(gt)  
		return guitars_found

	def match(self, gt , customer_gt):
		if gt.get_builder() != customer_gt.get_builder():
			return None
		
		if gt.get_model() != customer_gt.get_model():
			return None
		
		if gt.get_backwood() != customer_gt.get_backwood():
			return None

		if gt.get_type() != customer_gt.get_type():
			return None
		
		return True
