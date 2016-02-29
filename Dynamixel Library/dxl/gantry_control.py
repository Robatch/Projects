from dxl.dxlchain import DxlChain 

# Gantry Control
# Designed for Dynamixel MX-106 Servos on the DASL Table Gantry
# Author: Joel Trubatch
# Notes: Might need to add X-sync if the motors do not track evenly
#		 May also need to add a secondary position update if there is skipping on long moves
#		 Need to flesh out input to handle more types better


# Variables
speed = 100 # 100 is Slow-ish range from 0-1023 with 0 being fullspeed, 1 is slowest.
running = 1 # While loop variable

home = [0,0,0]; 
homeX = home[0]
homeY = home[1]
homeZ = home[2]

mX = 0   # Motor IDs 
mX2 = 1
mY = 2
mZ = 3 

goX = homeX
goY = homeY
goZ = homeZ

# Functions for moves
def xMove( mX, mX2, goX, speed ):
	chain.goto( mX, goX, speed )
	chain.goto( mX2, goX, speed )
	return;

def yMove( mY, goY, speed ):
	chain.goto( mY, goY, speed )
	return;

def zMove( mZ, goZ, speed ):
	chain.goto(mZ, goZ, speed )
	return;

# Initialize Serial
chain = DxlChain("/dev/ttyUSB0", rate = 1000000)

# Initialize Motors
motors = chain.get_motor_list()
print motors

# Display Initial Position
currPosX = chain.get_position(mX)
currPosY = chain.get_position(mY)
currPosZ = chain.get_position(mZ)
currPos = [currPosX,currPosY,currPosZ]
print currPos

# Auto Home if Not at Home
if currPos != home:
	xMove()
	yMove()
	zMove()
print " Type home to return to zero positions "
print " Type x to exit "

# Input Based Control Loop
while ( running = 1 ):
	inputStr = raw_input("Enter Desired Position in x y z")
	if inputStr.isdigit():
		splitInput = inputStr.split()
		goX = int(splitInput[0])
		goY = int(splitInput[1])
		goZ = int(splitInput[2])
	elif inputStr == 'home':
		goX = homeX
		goY = homeY
		goZ = homeZ
	elif inputStr == 'x':
		running = 0

	else:
		print "Bad Input"

	print "Moving to: X ", goX, " Y ", goY, " Z ", goZ 
	xMove( goX )
	yMove( goY )
	ZMove( goZ )

	wait_stopped()

	print "New Position is: X ", currPosX, " Y ", currPosY, " Z " currPosZ

print "Exiting Controller"