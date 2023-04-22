import random

UserChoices = ["U", "UP", "R", "RIGHT", "D", "DOWN", "L", "LEFT", "S", "SEARCH", "M", "MISSION", "U", "USE", "I", "INVENTORY"]
UserInput = "test" # ALWAYS .UPPER UserInput
Inventory = ["Gear", "Spark Plug"]

def intro(): # prints intro to game, add more description
	print("You are a mechanic on one of the 'grandest' interstellar flights in history.\n")
	print("You must replace a valve on an ice miner on asteriod AST-R10B\n")
	input("Press Enter.")
	# something to elaborate just a tiny amount, then be like "suddenly"
	print("""
You awake from your sleeping pod and you are surrounded by bright, flashing lights with an alarm going off. You hear a robot-like voice speak to you.

“Wake up Mechanic! Something happened!"
 """)
	input("Press Enter.")
	print("""
"The Super Repair Laser broke in the Command Room! The parts are scattered across the space ship!"
""")
	input("Press Enter.")
	mission()

def mission(): # Prints mission from start of game
	print("\nThe Super Repair Laser needs Gear, Spark Plug, Light Emitting Diode, and Duct Tape. They are located in the following areas:")
	print("Gear            >> Engine Room (Up)")
	print("Spark Plug      >> Barracks (Right)")
	print("LED             >> Break Room (Down)")
	print("Duct Tape       >> Ship Dock (Left)")
	print("--type “Mission” or “M” at any time to bring this menu back--")

def inventory(): # DOES NOT WORK, REFUSES TO ITERATE THROUGH MY JANK INVENTORY
	inventoryList = " "
	print("You have the following in your inventory:")
	for i in range(len(Inventory)): # list is not iritable for some reason
		if i == "":
			print("Nothing!!")
			print("Run around to find the missing parts! Use H or Help if you are lost.")
		inventoryList += print(Inventory[i])
	return inventoryList

def choice(): # checks if user choice is valid
	UserInput = input("What are you going to do Mechanic?\n").upper()
	while UserInput not in UserChoices:
		print("Not Valid input")
		UserInput = input("What are you going to do Mechanic?\n")
	# if statements for special inputs (not directions)
	if UserInput == UserChoices[10] or UserInput == UserChoices[11]: # if user input is mission, print mission
		mission()
	elif UserInput == UserChoices[8] or UserInput == UserChoices[9]: # if user input is search
		pass
	elif UserInput == UserChoices[14] or UserInput == UserChoices[15]: # if user input is inventory
		inventory()
	return UserInput

class Hallways():
	pass
	# init for player location?
	# if random range in like 1 - divisble by four:
	# print associated text
	# create objects for special text?
	# idk if thatd work

class Rooms():
	pass
	# room have text
	# room have value for loot
	# room have random for the random items

def end_game():
	pass
	# if player has things in inventory
	# open command room
	# dialogue and what not

# RUN GAME ------------------------------------------------------
# intro()
UserInput = choice()
print(UserInput) # sees if its saving the input right
# get user input
# depending on user input, run room function
# need to track location
# room function depends on location