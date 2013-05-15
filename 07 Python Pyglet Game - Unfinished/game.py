#create a dictionary to store the inventory of things we pick up
#different colored gems 
# add hearts
#complete maze
# out of bounds loops 
# create a small obstacle

import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 10
GAME_HEIGHT = 10


#### Put class definitions here ####
class Rock(GameElement):
	IMAGE = "Rock"
	SOLID = True

class Heart(GameElement):
	IMAGE = "Heart"

	def interact(self, player):
		player.inventory.append(self)
		GAME_BOARD.draw_msg("You just found a heart! You have %d items."%(len(player.inventory)))

class Key(GameElement):
	IMAGE = "Key"
	def interact(self, player):
		player.inventory.append(self)
		GAME_BOARD.draw_msg("Congratulations, you got the key! Now use it to open the treasure chest.")

# class OpenChest(GameElement):
# 	IMAGE = "OpenChest"
# 	SOLID =  False	

class OpenChest(GameElement):
	IMAGE = "OpenChest"


class Chest(GameElement):
	IMAGE = "Chest"
	SOLID = False
	def interact(self, player):
		player.inventory.append(self)
		GAME_BOARD.draw_msg("You just found the chest! Now use the key to open it up.")
		GAME_BOARD.del_el(chest.x, chest.y, CHEST)
		GAME_BOARD.set_el(9, 9, open_chest)
		GAME_BOARD.draw_msg("You win!")


		# if value (key) exists in list (inventory) print new message and show opened chest img


class Gem(GameElement):
	IMAGE = "BlueGem"

	def interact(self, player):
		player.inventory.append(self)
		GAME_BOARD.draw_msg("You just found a treasure! You have %d items."%(len(player.inventory)))

class Character(GameElement):
	IMAGE = "Princess"

	def __init__(self):
		GameElement.__init__(self)
		self.inventory = []


	def next_pos(self, direction):
		if direction == "up":
			return (self.x, self.y-1)
		elif direction == "down":
			return (self.x, self.y+1)
		elif direction == "left":
			return (self.x-1, self.y)
		elif direction == "right":
			return (self.x+1, self.y)
		return None

		

###   End class definitions    ####



def keyboard_handler():
	direction = None
	
	if KEYBOARD[key.UP]:
		direction = "up"
	if KEYBOARD[key.DOWN]:
		direction = "down"
	if KEYBOARD[key.LEFT]:
		direction = "left"
	if KEYBOARD[key.RIGHT]:
		direction = "right"



	if direction:
		next_location = PLAYER.next_pos(direction)

		if next_x > GAME_WIDTH -1 or next_y > GAME_WIDTH -1:

			print "test"

		existing_el = GAME_BOARD.get_el(next_x, next_y)
		if existing_el:
			existing_el.interact(PLAYER)

		if existing_el is None or not existing_el.SOLID:
			GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
			GAME_BOARD.set_el(next_x, next_y, PLAYER)




def initialize():
	global PLAYER
	PLAYER = Character()
	GAME_BOARD.register(PLAYER)
	GAME_BOARD.set_el(0, 0, PLAYER)
	print PLAYER

	global CHEST
	CHEST = OpenChest()
	GAME_BOARD.register(CHEST)

	rock_positions = [
		(0, 2),
		(1, 2),
		(3, 0),
		(3, 1),
		(3, 2),
		(3, 3),
		(4, 4),
		(4, 5),
		(4, 6),
		(3, 6),
		(2, 6),
		(1, 6),
		(1, 4),
		(1, 5),
		(1, 3)

	]

	rocks = []

	for pos in rock_positions:
		rock = Rock()
		GAME_BOARD.register(rock)
		GAME_BOARD.set_el(pos[0], pos[1], rock)
		rocks.append(rock)

	rocks[-1].SOLID = False

	for rock in rocks:
		print rock

	GAME_BOARD.draw_msg("Collect all the treasures. Then put them into the chest to win!")
	blue_gem = Gem()
	GAME_BOARD.register(blue_gem)
	GAME_BOARD.set_el(4, 7, blue_gem)

	key = Key()
	GAME_BOARD.register(key)
	GAME_BOARD.set_el(5, 5, key)

	open_chest = OpenChest()
	GAME_BOARD.register(open_chest)

	chest_positions = [	
	(9,9)
	]
	chests = []

	for pos in chest_positions:
		chest = Chest()
		GAME_BOARD.register(chest)
		GAME_BOARD.set_el(pos[0], pos[1], chest)
		chests.append(chest)

	for chest in chests:
		print chest
	# chest = Chest()
	# GAME_BOARD.register(chest)
	# GAME_BOARD.set_el(9, 9, chest)

	heart_1 = Heart()
	GAME_BOARD.register(heart_1)
	GAME_BOARD.set_el(3, 5, heart_1)



				
			# 	GAME_BOARD.draw_msg("testing")
			# open_the_chest()
			
			



#	rock4 = Rock()
#	GAME_BOARD.register(rock4)
#	GAME_BOARD.set_el(4, 4, rock4)

#	rock5 = Rock()
#	GAME_BOARD.register(rock5
#	GAME_BOARD.set_el(5, 5, rock5)

# initialize() engine initializes by pulling the game.py 

# print "The first rock is at", (rock1.x, rock1.y)
# print "The second rock is at", (rock2.x, rock2.y)
# print "Rock 1 image", rock1.IMAGE 
# print "Rock 2 image", rock2.IMAGE


#    pass
