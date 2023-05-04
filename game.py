import random
import pickle

UserChoices = ["U", "UP", "R", "RIGHT", "D", "DOWN", "L", "LEFT", "S", "SEARCH", "M", "MISSION", "U", "USE", "I", "INVENTORY", "Q", "QUIT", "H", "HELP"]
UserInput = "test" # ALWAYS .UPPER UserInput
Inventory = []
info = Inventory
menu = """
	The Game!
----------------------------
N - Start New Game
L - Load Saved Game
S - Save Current Game
Q - Quit
	\n"""
BeenEngineBefore = False # awful, terrible flag names
BeenBarracksBefore = False
BeenBreakBefore = False
BeenDockBefore = False

def mainMenu(): # bad bad programming, bad logic here too, it's procrastination's child
	global info
	choice = input(menu).upper()
	while choice != 'Q':
		if choice == 'N': # start new file
			with open(f"saveFile.dat", "wb") as file: # write it
				print("New File Created!\n")
				print("-----------------")
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
				choice = input(menu).upper()
		elif choice == 'S': # save current file
			try:
				with open('saveFile.dat', 'wb') as file:
					pickle.dump(info, f) # DOES NOT WORK
			except:
				print("Current Game Cannot Save") # ENTERS HERE THEN LEAVES
				choice = input(menu).upper()
		else:
			print("Not Valid Input")
			choice = input(menu).upper()

def intro(): # prints intro to game, add more description
	print("You are a mechanic on one of the 'grandest' interstellar flights in history.")
	print("You must replace a valve in an ice miner on asteriod AST-R10B\n")
	input("Press Enter.\n")
	# something to elaborate just a tiny amount, then be like "suddenly"
	print("You awake from your sleeping pod and you are surrounded by bright, flashing lights with an alarm going off. You hear a robot-like voice speak to you.")
	print("Wake up Mechanic! Something happened!\n") # REMOVE VOICE DOESNT WORK NOT CONSISTENT
	input("Press Enter.\n")
	mission()

def mission(): # Prints mission from start of game
	print("The Super Repair Laser broke in the Command Room! The parts are scattered across the space ship!")
	print("You will need to Search through the ship to find the missing parts and locate the Command Room.")
	print("\nThe Super Repair Laser needs Gear, Spark Plug, Light Emitting Diode, and Duct Tape. They are located in the following areas:")
	print("Gear            >> Engine Room  >> U or Up")
	print("Spark Plug      >> Barracks     >> R or Right")
	print("LED             >> Break Room   >> D or Down")
	print("Duct Tape       >> Ship Dock    >> L or Left")
	print("--type “Mission” or “M” at any time to bring this menu back--")
	choice()

def help():
	print("These are all of the commands you can use:\n")
	print("""
	U or Up - Moves Up
	R or Right - Moves Right
	D or Down - Moves Down
	L or Left - Moves Left
	--
	S or Search - Searches current room for anything useful
	I or Inventory - Displays current items in inventory
	M or Mission - Prints Mission
	--
	Q or Quit - Return to Main Menu
	""")
	choice()

def inventory(): # HAVE INSTRUCTIONS TO OPEN INVENTORY WHEN FIRST FIND OBJECT
	inventoryList = " "
	print("You have the following in your inventory:")
	for i in range(len(Inventory)):
		if i == "":
			print("Nothing!!") # NOT PRINTING FOR SOME REASON WHEN INVENTORY IS EMPTY
			print("Run around to find the missing parts! Use H or Help if you are lost.")
		print(Inventory[i])
	#return inventoryList
	choice()

def random_loot():
	item = int(random.randrange(1, 12))
	if item == 1:
		print("You also find a rainbow sticker!")
		Inventory.append("RainbowSticker")
		print("Rainbow Sticker has been added to your inventory.")
	elif item == 2:
		print("You also found a dry granola bar!")
		Inventory.append("GranolaBar")
		print("A Granola Bar has been added to your inventory.")
	elif item == 3:
		print("You also found a pack of Band-Aids!")
		Inventory.append("BandAids")
		print("The Band-Aids have been added to your inventory.")
	elif item == 4:
		print("You also found Instant Ramen!")
		Inventory.append("InstantRamen")
		print("Instant Ramen has been added to your inventory.")
	elif item == 5:
		print("You also found Masking Tape!")
		Inventory.append("MaskingTape")
		print("Masking Tape has been added to your inventory.")
	elif item == 6:
		print("You also found a Mess Kit!")
		Inventory.append("MessKit")
		print("A Mess Kit has been added to your inventory.")
	else:
		pass

def choice(): # checks if user choice is valid
	UserInput = input("\nWhat are you going to do Mechanic?\t--Type H for help--\n").upper()
	while UserInput not in UserChoices:
		print("Not Valid Input")
		UserInput = input("\nWhat are you going to do Mechanic?\t--Type H for help--\n")
	# if statements for special inputs (not directions)
	if UserInput == UserChoices[10] or UserInput == UserChoices[11]: # if user input is mission, print mission
		mission()
	elif UserInput == UserChoices[14] or UserInput == UserChoices[15]: # if user input is inventory
		inventory()
	elif UserInput == UserChoices[16] or UserInput == UserChoices[17]: # quit to main menu
		quit()
	elif UserInput == UserChoices[18] or UserInput == UserChoices[19]: # print help menu
		help()
		# visually pleasing pause
	elif UserInput == 'U':
		engine_room()
	elif UserInput == 'R':
		barracks()
	elif UserInput == 'D':
		break_room()
	elif UserInput == 'L':
		ship_dock()
	else:
		return UserInput

def quit():
	confirm = input("Are you sure you want to save and quit? (Yes/No)\n").upper() # confirm quit
	if 'Y' in confirm:
		mainMenu()
	elif 'N' in confirm:
		print("Okay! Have fun!")
		choice()
	else:
		print("Not Valid Input")

# ROOM LINE ----------------------------------------------------------------------------------------------------
# using objects would make this process a million times easier and i dont know why i didnt start with them
# very proud that this at least works though and theres at least a little variation for 'gameplay'
def engine_room(): # IF THERES TIME, ADD FLAG FOR FOUND COMMAND ROOM INTO MISSION
	global BeenEngineBefore # need to make each room its own flag, need to also save to file DOESNT WORK RIGHT NOW
	thing = '' # god awful varible name, i'm too tired to think of another way to say "users choice"
	if BeenEngineBefore == False:
		print("You enter the Engine Room. The room is full of pipes and meters that all connect to the engine in the middle.")
		print("Behind the engine, you see a sliding door. It appears to be damaged. On the door, there is scratched paint that says 'Command Room'.")
		print("Over on the right side of the room, there is a pile of crates labelled 'Spare Parts'. Maybe that is useful?\n")
		thing = choice()
		BeenEngineBefore = True
	elif BeenEngineBefore == True:
		print("You enter the Engine Room. The pile of crates is to your right. The Command Room is ahead of you.")
		thing = choice()
	
	if thing == UserChoices[8] or thing == UserChoices[9]: # search crates
		print("You go through the crates. They are full of extra hosing, pipes, tape, and random nuts and bolts.")
		print("You start to give up when you see a shiny Gear at the bottom of the box!")
		Inventory.append("Gear") # ADD RANDOM OBJECTS FOR FUNSIES
		print("\nA Gear has been added to your inventory!")
		random_loot()
	
	if "Gear" in Inventory and "SparkPlug" in Inventory and "LED" in Inventory and "DuctTape" in Inventory:
		end_game()
	else:
		print("It seems you can't progress in this room anymore. You go back to your sleeping pod.")
	choice()

def barracks():
	global BeenBarracksBefore
	thing = ''
	if BeenBarracksBefore == False:
		print("You enter the Barracks. There are rows of empty sleeping pods on each side of you.")
		print("Scanning down the rows of sleeping pods you see an open one labelled 'Mechanic'. Very strange how you did not wake up here.")
		print("At the foot of the open sleeping pod there is a toolbox that is slighty ajar.")
		BeenBarracksBefore = True
		thing = choice()
	elif BeenBarracksBefore == True:
		print("You enter the Barracks. The mechanic's sleeping pod is on your left and the open toolbox is at its foot.")
		thing = choice()
	
	if thing == UserChoices[8] or thing == UserChoices[9]: # search toolbox
		print("\nYou approach the toolbox.")
		print("In the top row of dividers, you find a container labelled Spark Plugs.")
		print('You take put the Spark Plugs in your pocket.')
		Inventory.append("SparkPlug")
		print("\nSpark Plug has been added to your inventory!")
		random_loot()
		input("Press Enter.\n")
		print("You return back to your original sleeping pod.")
		choice()

def break_room():
	global BeenBreakBefore
	if BeenBreakBefore == False:
		thing = ''
		print("You enter the break room. There are tables throughout the room, each with a light hanging above it.")
		print("There are motivational posters on the walls, as well as 4 month old announcements that no one has bothered to take down.")
		print("To your left there seems to be an old salad bar. Next to it is an empty vending machine.")
		print("In the back corner of the room there is a box of lightbulbs on a table. Maybe the LED is there?")
		thing = choice()
	elif BeenBreakBefore == True:
		print("You enter the break room. The box of lightbulbs is in the back corner.")
		thing = choice()

	if thing == UserChoices[8] or thing == UserChoices[9]: # search crates
		print("You investigate the lightbulb box. The majority of them are incandesant, which is stupid for a spaceship.")
		print("At the bottom of the box, laying in all of its technological glory, you find an LED!")
		Inventory.append("LED") # ADD RANDOM OBJECTS FOR FUNSIES
		print("\nAn LED has been added to your inventory!")
		random_loot()
		choice()

def ship_dock():
	print("You have entered the Ship Dock! Annekke forgot to add descriptive text!")
	thing = choice()

def end_game():
	if "Gear" in Inventory and "SparkPlug" in Inventory and "LED" in Inventory and "DuctTape" in Inventory: # if plot important parts are in inventory
		print("After rumaging around the ship you have found all 4 parts.")
		print("You manage to force the Command Room door open.") # the front of the ship is damaged by an asteroid, you repair the laser and watch the ship be rebuilt in front of you
		# describe command room door opening
		# you see the broken repair laser
		# you fix it
	else: # else
		print("You are still missing required items! Keep exploring!") # tell player to collect items, describe door not working properly

# THIS IS THE CLASS LINE -----------------------------------------------------------

class infoToSave(object):

	def __init__(self):
		self.inventory = inventory
		# save BeenHereBefore flags

# RUN GAME ----------------------------------------------------------------------------------------------------------------------------------------
mainMenu()