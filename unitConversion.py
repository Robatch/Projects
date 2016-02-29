## Unit Conversion For Gantry Control and Alternate X Control
# Rotations and degrees to CM
# 0.088degree resolution for mx106 360/4096 (4095 is final position value from -28672 to 28672)
# plus minus 7 revolutions/1.1m on Y and Z Axes , 
# plus minus 17.5 revolutions/plus 2.759m on X Axis
 


pi = 3.141592
# Pulley Diameters in m
# X Axis
mxDia = 0.05
driveDia = 0.02
finalDia =  0.05

driveRatio= mxDia/driveDia
circ = pi * finalDia

def meter2xPos(xM, circ, driveRatio):
	goX = ((xM/circ)*4096)/driveRatio

# Y Axis
def meter2yPos(yM, circ):
	goY = ((yM/circ)*4096)

# Z Axis
def meter2yPos(zM, circ)
	goZ = ((zM/circ)*4096)


# Alternate X Control
def xMove(mX, mX2, )

