UserChoices = ["U", "UP", "R", "RIGHT", "D", "DOWN", "L", "LEFT", "S", "SEARCH", "M", "MISSION", "U", "USE", "I", "INVENTORY"]
UserInput = "0" # ALWAYS .UPPER UserInput
Inventory = []

def intro(): # prints intro to game, add more description
	print("You are a mechanic on one of the 'grandest' interstellar flights in history.")
	print("You must replace a valve on an ice miner on asteriod AST-R10B")
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

def choice(): # checks if user choice is valid
	UserInput = input("What are you going to do Mechanic?\n").upper() # try to add this here to make choice 1 function, doesnt work
	while UserInput not in UserChoices:
		print("Not Valid input")
		UserInput = input("What are you going to do Mechanic?\n")
	return UserInput # returns 0 for some reason

# RUN GAME ------------------------------------------------------
intro()
choice()
print(UserInput) # sees if its saving the input right
# get user input
# depending on user input, run room function
# need to track location
# room function depends on location