import random
import pickle
import time

UserChoices = ["U", "UP", "R", "RIGHT", "D", "DOWN", "L", "LEFT", "S", "SEARCH", "M", "MISSION", "E", "EAT", "I", "INVENTORY", "Q", "QUIT", "H", "HELP"] # indexes 12 and 13 are for easter egg
UserInput = "if you see this, it's not working" # ALWAYS .UPPER UserInput
Inventory = [] # copy paste for bug testing: 'Gear', 'Resistor', 'LED', 'DuctTape'
menu = """
	The Game!
	Main Menu
----------------------------
T - Tutorial
N - Start New Game
L - Load Saved Game
S - Save Current Game
Q - Quit
	\n"""
TutorialComplete = False
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
				with open(f"saveFile.dat", 'rb') as file:
					Inventory = pickle.load(file) # FIRST THING SAVED FIRST THING LOADED
					BeenBarracksBefore = pickle.load(file)
					BeenBreakBefore = pickle.load(file)
					BeenDockBefore = pickle.load(file)
					BeenEngineBefore = pickle.load(file)
					TutorialComplete = pickle.load(file)
					CurrentRoom = pickle.load(file)
					CommandRoomFound = pickle.load(file)
					if [] in Inventory:
						Inventory.remove([])
					print("Game Successfully Loaded!\n")
					print("-----------------")
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
	print("You are a crew member on the cargo ship, '5h-1P'.")
	print("Specifically, you are a skilled mechanic. And you have been tasked with repairing a vital valve on an ice miner ship located on asteroid AST-R10B,")
	print("a desolate and treacherous location in the outer reaches of our galaxy. \n")
	input("\nPress Enter.\n")
	print("Travelling to AST-R10B takes a few months so it requires you be in cryosleep. You have your own sleeping pod.")
	print("The 5h-1P is equipped with a special 'Super Repair Laser' so that if anything goes wrong in travel, you won't have to be awoken.")
	print("It is a very complex ship, and its better than the majority of ships you've been apart of.\n")
	input("\nPress Enter.\n")
	print("As you drift in and out of consciousness, you become aware of a persistent, high-pitched sound that gradually grows louder and more insistent.")
	print("It takes you a moment to realize that it's an alarm.\n")
	input("\nPress Enter.\n")
	print("You awaken with a start to the sound of blaring alarms. Your head is pounding, and your vision is blurred.")
	print("You find yourself in the middle of a circular room with four hallways branching off in different directions.")
	print("The walls are made of metallic material, and there are blinking lights and displays all around.")
	print("After a moment you realize that the ship has been damaged, and you have been awoken to repair it.\n")
	input("\nPress Enter.\n")
	mission()

def mission(): # Prints mission from start of game
	print("\nThe Super Repair Laser broke in the Command Room! The parts are scattered across the space ship!")
	print("You need to Search through the ship to find the missing parts.")
	print("\nThe Super Repair Laser needs Gear, Resistor, Light Emitting Diode, and Duct Tape. They are located in the following areas:")
	if 'Gear' in Inventory:
		print("Gear            >> Engine Room  >> U or Up    >> FOUND")
	else:
		print("Gear            >> Engine Room  >> U or Up")
	if 'Resistor' in Inventory:
		print("Resistor        >> Barracks     >> R or Right >> FOUND")
	else:
		print("Resistor        >> Barracks     >> R or Right")
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

def tutorial(): # Should I have made this its own file? probably. Did I? nope
	global Inventory
	thing = ''
	print("Welcome to The Game!\n")
	print("Your goal in The Game is to collect items around a spaceship.")
	print("""You can type these phrases for movement:
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
	print("When you want to save the game, type 'Q' or 'Quit' when prompted. Then say 'Y' or 'Yes'. Then Save.")
	input("Press Enter.\n")
	print("Let's Practice.")
	print()
	print("You are packing your bags before you begin your interstellar flight.")
	# more description
	print("In front of you, there is your hairbrush.")
	print("Type 'S' or 'Search' to pick it up.")
	thing = input("\nWhat would you like to do?\n").upper()
	while 'S' not in thing:
		print("Not quite! Type 'S' or 'Search' to pick up the hairbrush.")
		thing = input("\nWhat would you like to do?\n").upper()
	if 'S' in thing:
		Inventory.append("Hairbrush")
		print("'Hairbrush' has been added to your inventory!\n")
		print("Congrats you now know how to use the search function!")
		print("Hint: whenever you enter a room where you can use search, the description will end with a question.")
	input("\nPress Enter.\n")
	print("To see what you have in your inventory, type 'I' or 'Inventory'.")
	thing = input("\nWhat would you like to do?\n").upper()
	while 'I' not in thing:
		print("Not quite! Type 'I' or 'Inventory' to open your inventory.")
		thing = input("\nWhat would you like to do?\n").upper()
	if 'I' in thing:
		print(Inventory[0])
	print("\nCongrats! You can now open your inventory!")
	input("Press Enter.\n")
	print("You have packed your bags and are now ready to report to work for your flight.")
	print("In order to leave your room you have to move! Type 'U' or 'Up' to move through the doorway.")
	thing = input("\nWhat would you like to do?\n").upper()
	while 'U' not in thing:
		print("Not quite! Type 'U' or 'Up' to leave your room.")
		thing = input("\nWhat would you like to do?\n").upper()
	if 'U' in thing:
		print("As you step out of the bedroom, you find yourself in a hallway that is brightly lit by the sunlight streaming in through a window at the end.")
		print("The walls are painted a soft shade of beige, and there are several framed family photos hung on them.")
	print("Now that you are in the hallway, type 'R' or 'Right' to move down the hall to the kitchen.")
	thing = input("\nWhat would you like to do?\n").upper()
	while 'R' not in thing:
		print("Not quite! Type 'R' or 'Right' to move down the hall.")
		thing = input("\nWhat would you like to do?\n").upper()
	if 'R' in thing:
		print("As you descend the staircase, the warm glow of the living room invites you into the living room.")
		print("The walls of the living room are painted a warm, earthy tone, and there are several pieces of artwork adorning them.")
		print("There is a coffee table made of reclaimed wood sits in the center of the room.")
		print("The table is adorned with a vase of freshly cut flowers and a stack of magazines.")
	print("\nYou can successfully move around!")
	print("Throughout the game you will need to move 'Up', 'Down', 'Left', and 'Right'.") # why didnt I use cardinal directions you may ask? I have no idea, its too far to change it
	input("Press Enter.\n")
	print("You stand in your living room, gazing out at the world beyond through the big picture window. The sky is a soft shade of blue, and fluffy white clouds drift lazily by.")
	print("You think about the journey ahead of you, the unknown adventures waiting to be discovered on your interstellar trip.")
	print("You feel a mix of excitement and apprehension, wondering what lies in store.")
	input("Press Enter.\n")
	print("You have completed the tutorial!")
	print("If you ever get stuck during the game, you can type 'H' or 'Help' for a list of commands.") 
	print("Now onto the game!")
	TutorialComplete = True
	Inventory = [] # reset inventory to not have a hairbrush in it

def help():
	global CurrentRoom
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
	print("You are back in the Sleeping Pod.")
	CurrentRoom = 'SleepingPod'
	choice()

def inventory():
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
	global CurrentRoom
	UserInput = input("\n\nWhat are you going to do Mechanic?\t--Type H for help--\n").upper()
	while UserInput not in UserChoices or 'S' in UserInput and CurrentRoom == 'SleepingPod': # prevents player from searching outside of a room
		print("Not Valid Input")
		UserInput = input("\n\nWhat are you going to do Mechanic?\t--Type H for help--\n").upper()
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
	elif 'U' in UserInput and CurrentRoom == 'EngineRoom':
		end_game()
		CurrentRoom = "SleepingPod"
		# visually pleasing pause
	elif 'U' in UserInput and CurrentRoom == 'SleepingPod':
		engine_room()
	elif 'R' in UserInput and CurrentRoom == 'SleepingPod':
		barracks()
	elif 'D' in UserInput and CurrentRoom == 'SleepingPod':
		break_room()
	elif 'L' in UserInput and CurrentRoom == 'SleepingPod':
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

def engine_room():
	global BeenEngineBefore, CurrentRoom, CommandRoomFound
	CurrentRoom = 'EngineRoom'
	thing = '' # god awful varible name, i'm too tired to think of another way to say "users choice"
	if BeenEngineBefore == False:
		print("You enter the Engine Room.\nThe room is full of pipes and meters that all connect to the engine in the middle.")
		print("Behind the engine, you see a sliding door. It appears to be damaged. On the door, there is scratched paint that says 'Command Room'.")
		print("Over on the right side of the room, there is a pile of crates labelled 'Spare Parts'. Maybe that is useful?\n")
		thing = choice()
		BeenEngineBefore = True
		CommandRoomFound = True
	elif BeenEngineBefore == True:
		print("You enter the Engine Room.\nThe pile of crates is to your right. The Command Room is ahead of you.\n")
		if 'U' in thing:
			end_game()
		else:
			thing = choice()
	
	if thing == UserChoices[8] or thing == UserChoices[9]: # search crates
		print("You go through the crates. They are full of extra hosing, pipes, tape, and random nuts and bolts.")
		print("You start to give up when you see a shiny Gear at the bottom of the box!")
		Inventory.append("Gear")
		print("\nA Gear has been added to your inventory!\n")
		input("\nPress Enter\n") # sends player back to sleeping pod for choice to work
		print("You return back to your sleeping pod.\n")
		CurrentRoom = 'SleepingPod'
	choice()

def barracks():
	global BeenBarracksBefore, CurrentRoom
	CurrentRoom = 'Barracks'
	thing = ''
	if BeenBarracksBefore == False:
		print("You enter the Barracks.\n")
		print("The Barracks on 5H-1P is a compact yet efficient living space designed to accommodate the crew during their long interstellar journeys.")
		print("The interior of the Barracks is dimly lit, with soft blue LED lights illuminating the space.")
		print("The walls of the Barracks are lined with sleek cryogenic sleep pods, each pod designed to house a single occupant in a state of suspended animation.")
		print("Scanning down the rows of sleeping pods you see an open one labelled 'Mechanic'. Very strange how you did not wake up here.")
		print("At the foot of the Mechanic sleeping pod there is a toolbox that is slighty ajar. Maybe there's another gear?\n")
		BeenBarracksBefore = True
		thing = choice()
	elif BeenBarracksBefore == True:
		print("You enter the Barracks.\nThe Mechanic's sleeping pod is on your left and the open toolbox is at its foot.\n")
		thing = choice()
	
	if thing == UserChoices[8] or thing == UserChoices[9]: # search toolbox
		print("\nYou approach the toolbox.")
		print("In the top row of dividers, you find a container labelled Resistors.")
		print('You put the Resistors in your pocket.')
		Inventory.append("Resistor")
		print("\nResistor has been added to your inventory!\n")
		random_loot()
		input("\nPress Enter\n")
		print("You return back to your sleeping pod.\n")
		CurrentRoom = 'SleepingPod'
		choice()

def break_room(): # HAVE EASTER EGG IF DO SEARCH TWICE, FIND COFFEE MACHINE MAKE WAIT 90 SECONDS TO GET COFFEE
	global BeenBreakBefore, CurrentRoom
	CurrentRoom = 'BreakRoom'
	if BeenBreakBefore == False:
		thing = ''
		print("You enter the break room. There are tables throughout the room, each with a light hanging above it.")
		print("There are motivational posters on the walls, as well as 4 month old announcements that no one has bothered to take down.")
		print("To your left there seems to be an old salad bar. Next to it is an empty vending machine.")
		print("In the back corner of the room there is a box of lightbulbs on a table. Maybe the LED is there?\n")
		thing = choice()
	elif BeenBreakBefore == True: # TESTING STILL
		print("You enter the break room. The box of lightbulbs is in the back corner.\n")
		thing = choice()
		if thing == UserChoices[8] or thing == UserChoices[9]: # search crates
			thing2 = input("There is a coffee machine next to the vending machine. Would you like a cup of coffee? (Yes/No)")
			while 'N' not in thing2:
				print("You press the power button on the coffee machine. It starts boiling the water and making your coffee.")
				print("The screen says 'Making Coffee:")
				for i in range(30, 0, -1):
					print(f"Time Remaining: {i}")
					time.sleep(1)
				print("Your hot cup of coffee dispenses.")
				Inventory.append("Coffee")
			if 'N' in thing2:
				print("Good Choice.")
			else:
				print("Not Valid Input.")

	if thing == UserChoices[8] or thing == UserChoices[9]: # search boxes
		print("You investigate the lightbulb box. The majority of them are incandesant, which is stupid for a spaceship.")
		print("At the bottom of the box, laying in all of its technological glory, you find an LED!")
		Inventory.append("LED") # ADD RANDOM OBJECTS FOR FUNSIES
		print("\nAn LED has been added to your inventory!\n")
		random_loot()
		input("\nPress Enter.\n")
		print("You return back to your sleeping pod.\n")
		CurrentRoom = 'SleepingPod'
		choice()

def ship_dock():
	global CurrentRoom
	CurrentRoom = 'ShipDock'
	thing = ''
	randomNum = random.randrange(1, 10)
	if BeenDockBefore == False:
		print("The ship dock on this cargo vessel is a marvel of engineering, designed to accommodate a wide range of spacecraft and")
		print("provide a secure connection for transporting cargo")
		print("and personnel across the vast expanse of space.")
		print("As you enter the ship dock, you notice the smooth, polished surfaces of the walls and floors,")
		print("which are made of a durable, lightweight material that can withstand the rigors of space travel.")
		print("The ceiling of the dock is a curved dome, providing a panoramic view of the surrounding stars and galaxies.")
		print("Next to the door there is a table with duct tape on top of it. The duct tape stacked in tall towers, maybe the custodian was bored?\n")
		thing = choice()
	elif BeenDockBefore == True:
		print("The ship dock on this cargo vessel is a spacious, well-lit chamber equipped with advanced docking clamps and")
		print("mechanical arms that can securely lock onto a variety of ship designs.")
		print("To your right is the table with the towers of duct tape.\n")
		thing = choice()

	if thing == UserChoices[8] or thing == UserChoices[9]: # take the tape
		if randomNum == 4:
			print("You grab for the roll on the top, but change your mind and grab a roll from the middle.")
			print('The tower falls over.')
		else:
			print("You take a roll of duct tape from the top of the tower.")
		Inventory.append("DuctTape")
		print("\nDuct Tape has been added to your inventory!\n")
		random_loot()
		input("\nPress Enter.\n")
		print("You return back to your sleeping pod.\n")
		CurrentRoom = 'SleepingPod'
	thing = choice()

def end_game(): # NOT LEAVING GAME CORRECTLY
	global TutorialComplete
	complete1 = False
	complete2 = False
	complete3 = False
	complete4 = False
	thing = ''
	nerd = False
	burn = random.randrange(1, 10)
	UseableParts = ['G', 'GEAR', 'R', 'RESISTOR', 'L', 'LED', 'LIGHT EMITTING DIODE', 'D', 'DUCT TAPE']
	if "Gear" in Inventory and "Resistor" in Inventory and "LED" in Inventory and "DuctTape" in Inventory: # if plot important parts are in inventory
		print("After rumaging around the ship you have found all 4 parts.")
		print("You manage to force the Command Room door open.\n")
		input("\nPress Enter.\n")
		print("You see that the front of the ship has been damaged by an asteroid.")
		print("The Super Repair Laser is in several pieces, it's definitely broken.\n")
		print("You pull out the Gear, Resistor, LED, and Duct Tape.")
		while (complete1 != True) or (complete2 != True) or (complete3 != True) or (complete4 != True):
			thing = input("\n\nWhat would you like to use?\n").upper()
			if thing == UseableParts[0] or thing == UseableParts[1]:
				print('The pully system that moves the arm up and down is missing its gear.')
				print("You take the tread on the motor off, and replace the gear.")
				print("It will take a few seconds to tighten the bolt all the way.\n")
				for i in range(4, 0, -1):
					time.sleep(1)
				print("The bolt clicks as it is tightened into place.\n")
				complete1 = True
			if thing == UseableParts[2] or thing == UseableParts[3]:
				print("You don't really know what this does, but theres a spot in head of the laser where it seems to fit.")
				print("You put the Resistor into its hole.\n")
				complete2 = True
			if thing == UseableParts[4] or thing == UseableParts[5] or thing == UseableParts[6]:
				print("The tip of the laser needs an LED to turn on.")
				print("You insert the LED into the hole.\n")
				if burn == 2:
					print("The laser was on when it broke, the laser turns on and burns you.\n")
				if thing == UseableParts[6]:
					nerd = True
				complete3 = True
			if thing == UseableParts[7] or thing == UseableParts[8]:
				print("The body of the laser is damaged and there are parts coming off of the frame.")
				print("You unroll some duct tape and tape the body back together.\n")
				complete4 = True
		input("\nPress Enter.\n")
		print("\n\n\tYou have successfully repaired the laser!")
		print("It starts repairing the front of the space ship automatically.")
		print("You return back to your sleeping pod and go back to sleep.")
		input("\nPress Enter.\n")
		print("\n\n\n")
		str = 'Thank you for playing The Game. I hope you enjoyed it.'
		print(f"{str:^150}")
		str = 'All Programming was done by me.'
		print(f"{str:^150}")
		str = 'Thank you to Eric Burt for helping me debug my game, and to my siblings for playtesting.'
		print(f"{str:^150}")
		str = 'Thank you to ChatGPT for helping me write description.\n\n'
		print(f"{str:^150}")
		if TutorialComplete == False:
			print("\nYou completed the game without using the tutorial! Good job!\n")
		if nerd == True:
			print("\nYou are a nerd, you typed out 'Light Emitting Diode'.\n")
		if burn == 2:
			print("\nHa! You got burned!\n")
		exit() # game was not ever exiting right and this is killing me, this is my solution. I am aware that the problem lies in how all of my rooms are functions
		# to solve this issue I should have there be actual coordinates and directions for the players to go and not just simple functions
		# im too tired for that and all of my final projects are due at once for some reason
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

# text formatting NOTHING WIDER THAN 146 CHARACTERS