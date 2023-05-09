import random
import pickle
import time

UserChoices = ["U", "UP", "R", "RIGHT", "D", "DOWN", "L", "LEFT", "S", "SEARCH", "M", "MISSION", "E", "EAT", "I", "INVENTORY", "Q", "QUIT", "H", "HELP"] # indexes 12 and 13 are for easter egg
UserInput = "if you see this, it's not working" # ALWAYS .UPPER UserInput
Inventory = ['Gear', 'SparkPlug', 'LED', 'DuctTape']
menu = """
	The Game!
	Main Menu
----------------------------
T - Tutorial
N - Start New Game
L - Load Saved Game
S - Save Current Game
Q - Quit
	\n""" # NEED TO ADD TUTORIAL, WILL ADD TIME AND WILL SHOW SEARCH
TutorialComplete = False # ADD ACHEIVEMENT FOR FINISHING GAME WITHOUT TUTORIAL
BeenEngineBefore = False # awful, terrible flag names
BeenBarracksBefore = False
BeenBreakBefore = False
BeenDockBefore = False
CurrentRoom = 'SleepingPod'
CommandRoomFound = False

def mainMenu(): # bad bad programming and logic here, it's procrastination's child
	choice = ''
	while choice != 'Q':
		global Inventory, BeenBarracksBefore, BeenBreakBefore, BeenDockBefore, BeenEngineBefore, TutorialComplete, CurrentRoom, CommandRoomFound
		choice = input(menu).upper() # ask inside while loop so it asks again
		if choice == 'T':
			tutorial()
		if choice == 'N': # start new file
			with open(f"saveFile.dat", "wb") as file: # write it
				print("New File Created!\n")
				print("-----------------")
			intro()
		elif choice == 'L': # load existing file
			try:
				with open(f"saveFile.dat", 'rb') as file: # NEED TO MAKE CLASS USE THIS INFO THEN RUN MISSION ---------------------------
					Inventory = pickle.load(file) # FIRST THING SAVED FIRST THING LOADED
					BeenBarracksBefore = pickle.load(file)
					BeenBreakBefore = pickle.load(file)
					BeenDockBefore = pickle.load(file)
					BeenEngineBefore = pickle.load(file)
					TutorialComplete = pickle.load(file)
					CurrentRoom = pickle.load(file)
					CommandRoomFound = pickle.load(file)
					#Inventory = info.inventory #prints thing wrong
					if [] in Inventory:
						Inventory.remove([])
					print(inventory) # checks if loading works # NEEDS TO SAY GAME SUCCESSFULLY LOADED
					mission()
			except (EOFError, FileNotFoundError):
				print("Game file not found!")
				print("Try saving first, or opening a new game.")
		elif choice == 'S': # save current file
			#try:
			with open('saveFile.dat', 'wb') as file:
				#info = infoToSave
				pickle.dump(Inventory, file) # add all varibles to class then only save class
				pickle.dump(BeenBarracksBefore, file)
				pickle.dump(BeenBreakBefore, file)
				pickle.dump(BeenDockBefore, file)
				pickle.dump(BeenEngineBefore, file)
				pickle.dump(TutorialComplete, file)
				pickle.dump(CurrentRoom, file)
				pickle.dump(CommandRoomFound, file)
				print("Save Successful.")
			#except:
				#print("Current Game Cannot Save.")

def intro(): # prints intro to game, add more description
	print("You are a mechanic on one of the 'grandest' interstellar flights in history.")
	print("You must replace a valve in an ice miner on asteriod AST-R10B\n")
	input("Press Enter.\n")
	# something to elaborate just a tiny amount, then be like "suddenly"
	print("You awake in a hallway that connects to 4 rooms. There are bright lights flashing and alarms going off.")
	print("The ship has been damaged.\n") # REMOVE VOICE DOESNT WORK NOT CONSISTENT
	input("Press Enter.\n")
	mission()

def mission(): # Prints mission from start of game
	print("The Super Repair Laser broke in the Command Room! The parts are scattered across the space ship!")
	print("You need to Search through the ship to find the missing parts.")
	print("\nThe Super Repair Laser needs Gear, Spark Plug, Light Emitting Diode, and Duct Tape. They are located in the following areas:")
	if 'Gear' in Inventory:
		print("Gear            >> Engine Room  >> U or Up    >> FOUND")
	else:
		print("Gear            >> Engine Room  >> U or Up")
	if 'SparkPlug' in Inventory:
		print("Spark Plug      >> Barracks     >> R or Right >> FOUND")
	else:
		print("Spark Plug      >> Barracks     >> R or Right")
	if 'LED' in Inventory:
		print("LED             >> Break Room   >> D or Down  >> FOUND")
	else:
		print("LED             >> Break Room   >> D or Down")
	if 'DuctTape' in Inventory:
		print("Duct Tape       >> Ship Dock    >> L or Left  >> FOUND")
	else:
		print("Duct Tape       >> Ship Dock    >> L or Left")
	if CommandRoomFound == True:
		print("\tThe Command Room is above the Engine Room.")
	else:
		print("\tYou need to locate the Command Room.")
	print("--type “Mission” or “M” at any time to bring this menu back--")
	choice()

def tutorial(): # NOT DONE
	print("Welcome to The Game!\n")
	print("Your goal is to collect items around a spaceship.")
	print("""You can use these commands are for movement:
	U or Up    - Move Up 1 Room
	R or Right - Move Right 1 Room
	D or Down  - Move Down 1 Room
	L or Left  - Move Left 1 Room
	""")
	input("Press Enter.\n")
	print("""These are special commands you can use:
	H - Help: Brings up help menu of commands
	I - Inventory: Shows what you have in your inventory
	S - Search: Searches a room, there are questions at the end of rooms that you can search
	M - Mission: Brings up your mission again, contains the list of rooms and directions
	""")
	input("Press Enter.\n")
	# run an example encounter.
	print("Let's Practice.")
	print()
	print("You are packing your bags before you begin your interstellar flight.")
	# more description
	print("In front of you, there is your hairbrush.")
	# there is -- in front of you. grab it with search
	# open inventory to see what youve grabbed
	# do all the movement
	print("You have completed the tutorial! Now onto the game!")

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

def inventory(): # HAVE INSTRUCTIONS TO OPEN INVENTORY WHEN FIRST FIND OBJECT # MAKE PLAYER INTERACTABLE
	inventoryList = " "
	print("You have the following in your inventory:")
	for i in range(len(Inventory)):
		if i == "":
			print("Nothing!!") # NOT PRINTING FOR SOME REASON WHEN INVENTORY IS EMPTY
			print("Run around to find the missing parts! Use H or Help if you are lost.")
		print(Inventory[i])
	#return inventoryList
	choice()

def easter_egg(): # NOT DONE
	pass

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
	elif UserInput == UserChoices[12] or UserInput == UserChoices[13]: # easter egg
		easter_egg()
	elif UserInput == UserChoices[14] or UserInput == UserChoices[15]: # if user input is inventory
		inventory()
	elif UserInput == UserChoices[16] or UserInput == UserChoices[17]: # quit to main menu
		quit()
	elif UserInput == UserChoices[18] or UserInput == UserChoices[19]: # print help menu
		help()
	elif 'U' in UserInput and CurrentRoom == 'EngineRoom': # DOESNT RUN CORRECTLY
		end_game()
		# visually pleasing pause
	elif 'U' in UserInput:
		engine_room()
	elif 'R' in UserInput:
		barracks()
	elif 'D' in UserInput:
		break_room()
	elif 'L' in UserInput:
		ship_dock()
	else:
		return UserInput

def quit(): # REQUIRES 3 ATTEMPTS TO LEAVE FOR SOME REASON, AFTER SAVING AND LOADING NEW FILE
	confirm = input("Are you sure you want to save and quit? (Yes/No)\n").upper() # confirm quit
	if 'Y' in confirm:
		mainMenu()
	elif 'N' in confirm:
		print("Okay! Have fun!")
		choice()
	else:
		print("Not Valid Input")
		confirm = input("Are you sure you want to save and quit? (Yes/No)\n").upper()

# ROOM LINE ----------------------------------------------------------------------------------------------------
# using objects would make this process a million times easier and i dont know why i didnt start with them
# very proud that this at least works though and that theres at least a little variation for 'gameplay'
# IF THERES TIME MAKE ROOMS CLASSES, SAVE THIS VERSION THO ONCE COMPLETE

def engine_room(): # NEED TO ADD RETURN TO SLEEPING POD TEXT
	global BeenEngineBefore, CurrentRoom, CommandRoomFound
	CurrentRoom = 'EngineRoom'
	thing = '' # god awful varible name, i'm too tired to think of another way to say "users choice"
	if BeenEngineBefore == False:
		print("You enter the Engine Room. The room is full of pipes and meters that all connect to the engine in the middle.")
		print("Behind the engine, you see a sliding door. It appears to be damaged. On the door, there is scratched paint that says 'Command Room'.")
		print("Over on the right side of the room, there is a pile of crates labelled 'Spare Parts'. Maybe that is useful?\n")
		thing = choice()
		BeenEngineBefore = True
		CommandRoomFound = True
	elif BeenEngineBefore == True:
		print("You enter the Engine Room. The pile of crates is to your right. The Command Room is ahead of you.")
		thing = choice()
	
	if thing == UserChoices[8] or thing == UserChoices[9]: # search crates
		print("You go through the crates. They are full of extra hosing, pipes, tape, and random nuts and bolts.")
		print("You start to give up when you see a shiny Gear at the bottom of the box!")
		Inventory.append("Gear")
		print("\nA Gear has been added to your inventory!")
		# HERE
	choice()

def barracks():
	global BeenBarracksBefore
	thing = ''
	if BeenBarracksBefore == False:
		print("You enter the Barracks. There are rows of empty sleeping pods on each side of you.")
		print("Scanning down the rows of sleeping pods you see an open one labelled 'Mechanic'. Very strange how you did not wake up here.")
		print("At the foot of the open sleeping pod there is a toolbox that is slighty ajar. Maybe theres another gear?")
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

def break_room(): # HAVE EASTER EGG IF DO SEARCH TWICE, FIND COFFEE MACHINE MAKE WAIT 90 SECONDS TO GET COFFEE
	global BeenBreakBefore
	if BeenBreakBefore == False:
		thing = ''
		print("You enter the break room. There are tables throughout the room, each with a light hanging above it.")
		print("There are motivational posters on the walls, as well as 4 month old announcements that no one has bothered to take down.")
		print("To your left there seems to be an old salad bar. Next to it is an empty vending machine.")
		print("In the back corner of the room there is a box of lightbulbs on a table. Maybe the LED is there?")
		thing = choice()
	elif BeenBreakBefore == True: # TESTING STILL
		print("You enter the break room. The box of lightbulbs is in the back corner.")
		if thing == UserChoices[8] or thing == UserChoices[9]: # search crates
		thing2 = input("There is a coffee machine next to the vending machine. Would you like a cup of coffee? (Yes/No)")
			if 'Y' in thing2:
				print("You press the power button on the coffee machine. It starts boiling the water and making your coffee.")
				print("The screen says 'Making Coffee:")
				for i in range(30, 0, -1):
					print(f"Time Remaining: {i}")
					time.sleep(1)
				print("Your hot cup of coffee dispenses.")
				Inventory.append("Coffee")
		thing = choice()

	if thing == UserChoices[8] or thing == UserChoices[9]: # search boxes
		print("You investigate the lightbulb box. The majority of them are incandesant, which is stupid for a spaceship.")
		print("At the bottom of the box, laying in all of its technological glory, you find an LED!")
		Inventory.append("LED") # ADD RANDOM OBJECTS FOR FUNSIES
		print("\nAn LED has been added to your inventory!")
		random_loot()
		choice()

def ship_dock():
	print("You have entered the Ship Dock! Annekke forgot to add descriptive text!")
	thing = choice()

def end_game(): # CHEESE GAME TIME WITH 3 SECOND REPAIR TIMERS
	if "Gear" in Inventory and "SparkPlug" in Inventory and "LED" in Inventory and "DuctTape" in Inventory: # if plot important parts are in inventory
		print("After rumaging around the ship you have found all 4 parts.")
		print("You manage to force the Command Room door open.") # the front of the ship is damaged by an asteroid, you repair the laser and watch the ship be rebuilt in front of you
		# describe command room door opening
		# you see the broken repair laser
		# you fix it
		# have end game wrap up of what extras you got, if you completed without a tutorial, if you found the easter egg
	else: # else
		print("You are still missing required items! Keep exploring!") # tell player to collect items, describe door not working properly

# THIS IS THE CLASS LINE -----------------------------------------------------------

class infoToSave(object):
	def __init__(self):
		self.__inventory = Inventory
		self.__engine = BeenEngineBefore
		self.__barracks = BeenBarracksBefore
		self.__breakRoom = BeenBreakBefore
		self.__dock = BeenDockBefore
		self.__tutorial = TutorialComplete
		self.__room = CurrentRoom
		self.__commandFound = CommandRoomFound

	@property
	def inventory(self):
		return inventory

	@inventory.getter
	def inventory(self, newInventory):
		inventory = Inventory # need to flip everything else to be like this one, new = old
	
	@property
	def engine(self):
		return engine

	@engine.getter
	def engine(self, newEngine):
		engine = BeenEngineBefore
	
	@property
	def barracks(self):
		return barracks

	@barracks.getter
	def barracks(self, newBarracks):
		barracks = BeenBarracksBefore
	
	@property
	def breakRoom(self):
		return breakRoom

	@breakRoom.getter
	def breakRoom(self, newBreakRoom):
		breakRoom = BeenBreakBefore
	
	@property
	def dock(self):
		return barracks

	@dock.getter
	def dock(self, newDock):
		dock = BeenDockBefore
	
	@property
	def tutorial(self):
		return tutorial

	@tutorial.getter
	def tutorial(self, newTutorial):
		tutorial = TutorialComplete
	
	@property
	def room(self):
		return room
	
	@room.getter
	def room(self, newRoom):
		room = CurrentRoom
	
	@property
	def commandFound(self):
		return commandFound
	
	@commandFound.getter
	def commandFound(self, newCommandFound):
		commandFound = CommandRoomFound

# RUN GAME ----------------------------------------------------------------------------------------------------------------------------------------
mainMenu()
