import tkinter as tk
from items import *
class Player():
	def __init__(self,master=None):
		self.inventory = []
		self.hp = 10
		self.knowledge = 0
		self.money = tk.IntVar(master, 0)
		self.cauldron_contents = []

	def add_money(self,amount):
		current = self.money.get()
		self.money.set(current + amount)

	def knowledge_upgrade(self,potion):
		self.knowledge += 1

	def getting_damage(self,damage):
		if self.hp <= damage:
			return False
		else:
			self.hp -= damage
		return True

	def add_item(self, item):
		self.inventory.append(item)
		print(f"Picked up: {item.name}")

	def remove_item(self, item):
		if item in self.inventory:
			self.inventory.remove(item)

	def throw_into_cauldron(self, item):
		if item in self.inventory:
			self.remove_item(item)
			self.cauldron_contents.append(item)

	def craft_potion(self):
		#------------------simple example of potion crafting----------------
		ingredients = set([i.name for i in self.cauldron_contents])
		if len(ingredients) == 0:
			return		
		elif "feather" in ingredients and "lepidra" in ingredients and len(ingredients)==2:
			potion = Item("knowledge_potion",False)
		elif "blueberry" in ingredients and "dragonfly_wing" in ingredients and len(ingredients)==2:
			potion = Item("invisibility_potion",False)
		elif "black_feather" in ingredients and "brown_feather" in ingredients and "feather" in ingredients and "bone" in ingredients and len(ingredients)==4:
			potion = Item("toxin",False)
		else:
			potion = Item("ruined_potion",False)
		self.cauldron_contents.clear()
		self.add_item(potion)
		return potion