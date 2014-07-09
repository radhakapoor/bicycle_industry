
class Wheel(object):	
	
	def __init__(self, wheel_name, wheel_weight, wheel_cost):
		self.wheel_name = wheel_name
		self.wheel_weight = wheel_weight
		self.wheel_cost = wheel_cost

	def __repr__ (self):
		return "wheel model name is {}, wheel weight is {}lbs per wheel, wheel manufacturing cost is ${}.00 per wheel".format(self.wheel_name, self.wheel_weight, self.wheel_cost)
	
	
class Frame(object):
	ALUMINIUM_TYPE = 1
	STEEL_TYPE = 2
	CARBON_TYPE = 3 

	def __init__(self, frame_weight, frame_cost, frame_code):
		self.frame_weight = frame_weight
		self.frame_cost = frame_cost
		if frame_code == Frame.ALUMINIUM_TYPE:
			self.material = "aluminium"
		elif frame_code == Frame.STEEL_TYPE:
			self.material = "steel"
		else:
			self.material = "carbon"		

	def __repr__(self):
		return "frame is made of {}, weight of the frame is {}lbs and manufacturing cost of the frame is ${}.00".format(self.material, self.frame_weight, self.frame_cost)

class Bicycle(object):
	
	def __init__(self, wheel_name, wheel_weight, wheel_cost, frame_weight, frame_cost, frame_code, bicycle_name, manufacturer):
		self.wheel = Wheel(wheel_name, wheel_weight, wheel_cost)
		self.frame = Frame(frame_weight, frame_cost, frame_code)
		self.bicycle_name = bicycle_name
		self.manufacturer = manufacturer

	def __repr__(self):
		return "The name of the bicycle model is {}, the manufacturer of the bicycle model is {}, the bicycle model's {}, the bicycle model's {}\n".format(self.bicycle_name, self.manufacturer, self.wheel, self.frame)

	def total_weight(self, wheel_weight, frame_weight):		
		total_weight = (wheel_weight * 2) + frame_weight
		return "The total weight of the bike is {}lbs".format(total_weight)

	def total_cost(self, wheel_cost, frame_cost):
		total_cost = (wheel_cost * 2) + frame_cost 
		return "The total cost of the bike is ${}.00".format(total_cost)


class Manufacturer(object):

	models = []

	def __init__(self, manufacturer_name, manufacturer_margin, models):
		self.manufacturer_name = manufacturer_name
		self.manufacturer_margin = manufacturer_margin
		self.models = models
	
	def __repr__(self):
		return 'name of the manufacturer is {}, manufacturer margin is {}, the models it manufacturers are {}'.format(self.manufacturer_name, self.manufacturer_margin, self.models)
	
	
class BikeShop(object):

	inventory = []

	def __init__(self, bikeshop_name, retail_margin, inventory):
		self.bikeshop_name = bikeshop_name
		self.retail_margin = retail_margin
		self.inventory = inventory

	def __repr__(self):
		return 'name of the bike shop is {}, bike shop margin is {}, bike shop\'s inventory is {}'.format(self.bikeshop_name, self.retail_margin, self.inventory)
	
	"""
	can see how much profit they have made on margin from selling bikes 
	"""		
	def profit(self):
		pass
	
class Customer(object):
	
	def __init__(self, customer_name, budget):
		self.customer_name = customer_name
		self.budget = budget

	def __repr__(self):
		return 'name of the customer is {}, customer\'s budget is {}'.format(self.customer_name, self.budget)






