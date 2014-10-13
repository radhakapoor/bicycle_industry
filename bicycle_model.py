
class Wheel(object):    	
	
	def __init__(self, name, weight, cost):
		self.name = name
		self.weight = weight
		self.cost = cost			  		
	
		
class Frame(object):	
	ALUMINIUM_TYPE = 1
	STEEL_TYPE = 2
	CARBON_TYPE = 3 

	def __init__(self, weight, cost, code):
		self.weight = weight
		self.cost = cost
		if code == Frame.ALUMINIUM_TYPE:
			self.material = "aluminium"
		elif code == Frame.STEEL_TYPE:
			self.material = "steel"
		else:
			self.material = "carbon"			


class Bicycle(object):
	serial_generator = iter(range(1000))
	
	def __init__(self, wheel, frame, name, manufacturer, manufacturer_margin):
		self.wheel = wheel
		self.frame = frame
		self.name = name
		self.manufacturer = manufacturer
		self.manufacturer_margin = manufacturer_margin
		self.serial = next(self.serial_generator)		

	def __repr__(self):
  		return "model {} serial number: {}".format(self.name, self.serial)    

	def total_weight(self):		
		total_weight = (self.wheel.weight * 2) + self.frame.weight
		return total_weight

	def total_cost(self):
		parts_cost = (self.wheel.cost * 2) + self.frame.cost
		total_cost = parts_cost + (parts_cost * self.manufacturer_margin)
		return total_cost


class Manufacturer(object):

	models = []

	def __init__(self, name, manufacturer_margin, models):
		self.name = name
		self.manufacturer_margin = manufacturer_margin		
		self.models = models

	
class BikeShop(object):

	inventory = []
	sold = []

	def __init__(self, name, retail_margin, inventory):
		self.name = name
		self.retail_margin = retail_margin
		self.inventory = inventory		
	
	def inventory_value(self):
		"""total cost of wholesale bike shop's inventory"""
		cost = 0
		for bike in self.inventory:
			cost = cost + bike.total_cost()
		return cost
	
	def sell_bike(self, i):
		"""add bike at inventory index i to sold list"""
		if i < len(self.inventory):
			self.sold.append(self.inventory[i])
		else:
			print "That bike is not in stock"
		
	def profit(self):
		"""profit from sold bikes"""
		retail_value = 0
		wholesale_value = 0
		for bike in self.sold:
			retail_value += bike.total_cost() + (self.retail_margin * bike.total_cost())
			wholesale_value += bike.total_cost() 
		return retail_value - wholesale_value

	def bikeweight(self):
		"""name, weight of each bike in the bikeshop inventory"""
		for bike in self.inventory:
			print "{}, total weight is {}lbs\n".format(bike, bike.total_weight())	
	
	def affordable_bikes(self, customer):		
		"""lists bikes the customer can afford within their budget, customer purchases most expensive within budget"""
		affordable_bikes = []				
		for bike in self.inventory:
			price = bike.total_cost() + (self.retail_margin * bike.total_cost())
			if customer.fund >= price:
				paid = price
				customer_fund_balance = customer.fund - paid				
				affordable_bikes.append(bike)				
				purchase = affordable_bikes[-1]		
				print "{} can afford {} for ${}".format(customer.name, bike, paid)				
		self.sold.append(purchase)		
		return "{} buys {} for ${} and her fund balance is ${}\n".format(customer.name, purchase, paid, customer_fund_balance)

	def remaining_inventory(self):
		"""remove sold bikes from bikeshop inventory"""
		for bike in self.sold:
			if bike in self.inventory:
				self.inventory.remove(bike)
		print "{}'s remaining inventory is: {}".format(self.name, self.inventory)

class Customer(object):
	
	def __init__(self, name, fund):
		self.name = name
		self.fund = fund

	
	










