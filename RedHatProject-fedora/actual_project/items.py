import random

class Item():
	def __init__(self,name,	ingredient, cost=1):				#ingredient = True/False
		self.name = name
		self.ingredient = ingredient				#doesnt actually work just a concept for future
		self.cost = cost

def random_item():
	items = [
		Item("feather", True,5),
        Item("butterfly_wing", True,7),
        Item("blueberry", True,4),
		Item("redberry",True,3),
		Item("bone",True,5),
		Item("lepidra",True,2),
		Item("dragonfly_wing",True,15),
		Item("black_feather",True,10),
		Item("brown_feather",True,8),
		Item("health_potion",False,40)
		]
	
	return random.choice(items)