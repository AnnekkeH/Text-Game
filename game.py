import random

UserChoices = ["U", "UP", "R", "RIGHT", "D", "DOWN", "L", "LEFT", "S", "SEARCH", "M", "MISSION", "U", "USE", "I", "INVENTORY", "Q", "QUIT"]
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
	print("--type “Quit” or “Q” at at any time to save and quit--")

def inventory(): # DOES NOT WORK, REFUSES TO ITERATE THROUGH MY JANK INVENTORY
	inventoryList = " "
	print("You have the following in your inventory:")
	for i in range(len(Inventory)): # list is not iritable for some reason
		if i == "":
			print("Nothing!!")
			print("Run around to find the missing parts! Use H or Help if you are lost.")
		print(Inventory[i])
	return inventoryList

def quit():
	confirm = input("Are you sure you want to save and quit? (Yes/No)").upper() # confirm quit
	if 'Y' in confirm:
		name = input("What do you want to name your save file?") # get name of file
		with open(f"{name}.txt", "w") as file: # write it
		file.write(f"{inventory}\n") # add info (inventory, active room location, parts)
	elif 'N' in confirm:
		print("Okay! Have fun!")
	else:
		print("Not Valid Input")
	# save game to file
	# quit

def choice(): # checks if user choice is valid
	UserInput = input("What are you going to do Mechanic?\n").upper()
	while UserInput not in UserChoices:
		print("Not Valid Input")
		UserInput = input("What are you going to do Mechanic?\n")
	# if statements for special inputs (not directions)
	if UserInput == UserChoices[10] or UserInput == UserChoices[11]: # if user input is mission, print mission
		mission()
	elif UserInput == UserChoices[14] or UserInput == UserChoices[15]: # if user input is inventory
		inventory()
	if UserInput == UserChoices[16] or UserInput == UserChoices[17]:
		quit()
	return UserInput

class Rooms(object):
	Enter = False # one way flag for first entering room
	Parts = [] # list of plot important parts
	# need to make loot function that randomizes loot and adds it to parts
	
	def __init__(self, name, parts, loot):
		Enter = True
		self.RoomName = name
		self.Parts = parts # not sure i need these, might make loot a function that adds to parts

		roomText = random.randrange(1, 4) # pick random text for first entering room
		if roomText == 1:
			print("room text 1")
		elif roomText == 2:
			print("room text 2")
		elif roomText == 3:
			print("room text 3")
		else:
			"You dun goofed"

	def __str__(self):
		pass
		# print room text with like 2 variations
	# room have text
	# room have value for loot
	# room have random for the random items

class Hallways(Rooms):
	pass
	# use same Init code with different input text, have like 8 possible text descriptions

# need to make save option

def end_game():
	pass
	if Gear in inventory and SparkPlug in inventory and LED in inventory and DuctTape in inventory: # if plot important parts are in inventory
		print("woo")
		# describe command room door opening
		# you see the broken repair laser
		# you fix it
		# dragon
		# pre-scripted fight
	else: # else
		print("You are still missing required items! Keep exploring!") # tell player to collect items

# RUN GAME ----------------------------------------------------------------------------------------------------------------------------------------
# intro()
UserInput = choice()
# print(UserInput) # CHECKS USER INPUT

# if user input == U:
	# print engine room
# elif user input == R:
	# print barracks
# elif user input == D:
	# print Break room
# elif user input = L:
	# print Ship dock
