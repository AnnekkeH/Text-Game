UserChoices = [{"U", "UP"}, {"R", "RIGHT"}, {"D", "DOWN"}, {"L", "LEFT"}, {"S", "SEARCH"}, {"M", "MISSION"}, {"U", "USE"}, {"I", "INVENTORY"}]
UserInput = 0 # ALWAYS .UPPER UserInput

def Intro(): # prints intro to game, add more description
	print("""
You awake from your sleeping pod and you are surrounded by bright, flashing lights. There is an alarm going off. You hear a robot-like voice speak to you.

“Wake up Mechanic! Something happened!"
""")
	input("Press Enter.\n")
	print("""
"The Super Repair Laser broke in the Command Room! The parts are scattered across the space ship!"
""")
	input("Press Enter.\n")

def Mission(): # Prints mission from start of game
	print("""
The Super Repair Laser needs Gear, Spark Plug, Light Emitting Diode, and Duct Tape. They are located in the following areas:
	Gear            >> Engine Room
	Spark Plug      >> Barracks
	LED             >> Break Room
	Duct Tape       >> Ship Dock

–type “Mission” or “M” at any time to bring this menu back–""")

def Help(): # prints Help Menu (commands)
	print("""
COMMANDS:\t\t\tAll can be shortened to First Letter
	Up
	Right
	Down
	Left
	Search
	Mission
	Use
	Inventory
	""") # make hint function with room functions

def Choice(): # what are you going to do mechanic
	UserInput = input("What are you going to do Mechanic?\n")
	UserInput = UserInput.upper
	return UserInput

Intro()
Mission()
Choice()
while UserInput in UserChoices:
	if UserInput == "M":
		print("yipeeee")
	else:
		print("Not A Valid Input.")