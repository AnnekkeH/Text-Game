UserChoices = ["U", "UP", "R", "RIGHT", "D", "DOWN", "L", "LEFT", "S", "SEARCH", "M", "MISSION", "U", "USE", "I", "INVENTORY"]
UserInput = "0" # ALWAYS .UPPER UserInput
Inventory = []

def intro(): # prints intro to game, add more description
	print("""
 You awake from your sleeping pod and you are surrounded by bright, flashing lights. There is an alarm going off. You hear a robot-like voice speak to you.

 “Wake up Mechanic! Something happened!"
 """)
	input("Press Enter.")
	print("""
 "The Super Repair Laser broke in the Command Room! The parts are scattered across the space ship!"
 """)
	input("Press Enter.")

def mission(): # Prints mission from start of game
	print("\mThe Super Repair Laser needs Gear, Spark Plug, Light Emitting Diode, and Duct Tape. They are located in the following areas:")
	print("Gear            >> Engine Room")
	print("Spark Plug      >> Barracks")
	print("LED             >> Break Room")
	print("Duct Tape       >> Ship Dock")
	print("–type “Mission” or “M” at any time to bring this menu back–")

def choice(UserInput): # checks if user choice is valid
	while UserInput not in UserChoices:
		print("Not Valid input")
		UserInput = input("What are you going to do Mechanic?\n")
	return UserInput

UserInput = input("What are you going to do Mechanic?\n")
choice(UserInput)
print(UserInput) # sees if its saving the input right
# get user input
# depending on user input, run room function
# need to track location
# room function depends on location