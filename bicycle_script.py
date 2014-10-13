
from bicycle_model import Bicycle, Wheel, Frame, Manufacturer, BikeShop, Customer

"""helper functions to create new wheels"""
def new_slick():
	return Wheel('Slick', 9, 14)

def new_medium():
	return Wheel('Medium', 6, 16)

def new_hard():
	return Wheel('Hard', 3, 125)

"""helper functions to create new frames"""
def new_aluminium():
	return Frame(40, 30, 1)

def new_steel():
	return Frame(30, 75, 2)

def new_carbon():
	return Frame(15, 300, 3)


"""helper functions to create new bicyles"""

def new_champion():
	return Bicycle(new_slick(), new_aluminium(), 'Champion', 'Eagle', 0.1)

def new_tour():
	return Bicycle(new_medium(), new_steel(), 'Tour', 'Eagle', 0.1)

def new_speedy():
	return Bicycle(new_medium(), new_carbon(), 'Speedy', 'Eagle', 0.1)

def new_roadrage():
	return Bicycle(new_slick(), new_aluminium(), 'RoadRage', 'Seagull', 0.2)

def new_monsterhill():
	return Bicycle(new_slick(), new_carbon(), 'MonsterHill', 'Seagull', 0.2)

def new_giro():
	return Bicycle(new_hard(), new_carbon(), 'Giro', 'Seagull', 0.2)

"""create 2 manufacturers"""
manufacturer_one = Manufacturer('Eagle', 0.1, ['Champion', 'Tour', 'Speedy'])
manufacturer_two = Manufacturer('Seagull', 0.2, ['Roadrage', 'Monsterhill', 'Giro'])


"""create 1 bike shop"""
bikeshop_one = BikeShop('East Village Shop', 0.2, [new_champion(), new_tour(), new_tour(), new_speedy(), 
							new_speedy(), new_roadrage(), new_roadrage(), new_monsterhill(), new_monsterhill(), new_giro()])

"""create 3 customers"""
customer_one = Customer('Sarah', 200)
customer_two = Customer('Ella', 500)
customer_three = Customer('Hannah', 1000)


customers = [customer_one, customer_two, customer_three]

"""print out name and total weight of each bicycle model carried by the bike shop"""
bikeshop_one.bikeweight()

"""print out a list of bikes that the customers can afford given their budget, customer purchases one and prints out their fund balance"""
for c in customers:
	print bikeshop_one.affordable_bikes(c)

"""print out bikeshop's initial inventory"""
print "{}'s initial inventory is: {}\n".format(bikeshop_one.name, bikeshop_one.inventory)

"""prints out bikeshop's remaining inventory"""
bikeshop_one.remaining_inventory()

"""bikes shop calculates profit made on sold bikes"""
print "{}'s profit from the sale of the three bikes is ${}\n".format(bikeshop_one.name, bikeshop_one.profit())

















