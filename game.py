import random
import pickle

UserChoices = ["U", "UP", "R", "RIGHT", "D", "DOWN", "L", "LEFT", "S", "SEARCH", "M", "MISSION", "U", "USE", "I", "INVENTORY", "Q", "QUIT"]
UserInput = "test" # ALWAYS .UPPER UserInput
Inventory = []
info = Inventory
BeenHereBefore = False

def mainMenu(): # bad bad programming, bad logic here too, it's procrastination's child
	global info
	choice = input("""
	The Game!
----------------------------
N - Start New Game
L - Load Saved Game
S - Save Current Game
Q - Quit
	\n""").upper()
	while choice != 'Q':
		if choice == 'N': # start new file
			with open(f"saveFile.dat", "wb") as file: # write it
				print("New File Created!\n") # add inventory and room status
			intro()
			break
		elif choice == 'L': # load existing file
			try:
				with open(f"saveFile.dat", 'rb') as file:
					inventory = pickle.load(file)
					print(inventory) # checks if loading works
					break
			except FileNotFoundError as e:
				print("Game file not found!")
				print("Try saving first, or opening a new game.")
				print(e)
				choice = input("""
	The Game!
----------------------------
N - Start New Game
L - Load Saved Game
S - Save Current Game
Q - Quit
	\n""").upper()
		elif choice == 'S': # save current file, DONT FORGET TO SAVE BeenHereBefore
			try:
				with open('saveFile.dat', 'wb') as file:
					pickle.dump(info, f) # DOES NOT WORK
			except:
				print("Current Game Cannot Save") # ENTERS HERE THEN LEAVES
				choice = input("""
	The Game!
----------------------------
N - Start New Game
L - Load Saved Game
S - Save Current Game
Q - Quit
	\n""").upper()
		else:
			print("Not Valid Input")
			choice = input("""
	The Game!
----------------------------
N - Start New Game
L - Load Saved Game
S - Save Current Game
Q - Quit
	\n""").upper()

def intro(): # prints intro to game, add more description
	print("You are a mechanic on one of the 'grandest' interstellar flights in history.\n")
	print("You must replace a valve in an ice miner on asteriod AST-R10B\n")
	input("Press Enter.\n")
	# something to elaborate just a tiny amount, then be like "suddenly"
	print("You awake from your sleeping pod and you are surrounded by bright, flashing lights with an alarm going off. You hear a robot-like voice speak to you.\n")
	print("Wake up Mechanic! Something happened!\n")
	input("Press Enter.\n")
	print("The Super Repair Laser broke in the Command Room! The parts are scattered across the space ship!\n")
	input("Press Enter.\n")
	mission()

def mission(): # Prints mission from start of game
	print("\nThe Super Repair Laser needs Gear, Spark Plug, Light Emitting Diode, and Duct Tape. They are located in the following areas:")
	print("Gear            >> Engine Room (Up)")
	print("Spark Plug      >> Barracks (Right)")
	print("LED             >> Break Room (Down)")
	print("Duct Tape       >> Ship Dock (Left)")
	print("--type “Mission” or “M” at any time to bring this menu back--")
	print("--type “Quit” or “Q” at at any time to save and quit--")
	choice()

def inventory(): # HAVE INSTRUCTIONS TO OPEN INVENTORY WHEN FIRST FIND OBJECT
	inventoryList = " "
	print("You have the following in your inventory:")
	for i in range(len(Inventory)):
		if i == "":
			print("Nothing!!")
			print("Run around to find the missing parts! Use H or Help if you are lost.")
		print(Inventory[i])
	return inventoryList

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
	elif UserInput == UserChoices[16] or UserInput == UserChoices[17]:
		quit()
	# visually pleasing pause
	if UserInput == 'U':
		engine_room()
	elif UserInput == 'R':
		barracks()
	elif UserInput == 'D':
		break_room()
	elif UserInput == 'L':
		ship_dock()
	return UserInput

def quit():
	confirm = input("Are you sure you want to save and quit? (Yes/No)\n").upper() # confirm quit
	if 'Y' in confirm:
		mainMenu()
	elif 'N' in confirm:
		print("Okay! Have fun!")
	else:
		print("Not Valid Input")

# -- make each room a function, only call function based on user input in choice() --
def engine_room():
	global BeenHereBefore # need to make each room its own flag, need to also save to file
	if BeenHereBefore == False:
		print("You have entered the Engine Room! Annekke forgot to add descriptive text!") # describe command room door add emphasis to searchable thing
		BeenHereBefore = True
	elif BeenHereBefore == True:
		print("You've Been Here Before! Annekke forgot to add descriptive text!")
	# search it
	# add to inventory
	# describe leaving
	# leave, return inventory
	choice()

def barracks():
	print("You have entered the Barracks! Annekke forgot to add descriptive text!")
	choice()

def break_room():
	print("You have entered the Break Room! Annekke forgot to add descriptive text!")
	choice()

def ship_dock():
	print("You have entered the Ship Dock! Annekke forgot to add descriptive text!")
	choice()

def end_game():
	if Gear in inventory and SparkPlug in inventory and LED in inventory and DuctTape in inventory: # if plot important parts are in inventory
		print("woo")
		# describe command room door opening
		# you see the broken repair laser
		# you fix it
	else: # else
		print("You are still missing required items! Keep exploring!") # tell player to collect items, describe door not working properly

# THIS IS THE CLASS LINE -----------------------------------------------------------

class infoToSave(object):

	def __init__(self):
		self.inventory = inventory

# RUN GAME ----------------------------------------------------------------------------------------------------------------------------------------
mainMenu()