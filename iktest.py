# IK for Gantry with Manipulator
# Assumes X Positive is Away from Gantry Computer
# Right hand Coord System, index Finger X, Z Pos Down
# Y positive is "right" if facing in X positive direction
# Spherical Coords for relation between object and joint 2(pitch)
# With Tip of end effector being at object defining orientation
# XY Plain is 0 for phi Z positive = phi positive
# X positive is 0 for theta, CCW is positive
import math 
phi = float(raw_input("enter phi"))
theta = float(raw_input("enter theta"))
xObj = float(raw_input("enter x"))
yObj = float(raw_input("enter y"))
zObj = float(raw_input("enter z"))

a = 5
b = 10

theta_r = math.radians(theta)
phi_r = math.radians(phi)


x = b * math.cos(theta_r)*math.sin(phi_r) + xObj

y = b * math.sin(theta_r)*math.sin(phi_r) + yObj

z = (b * math.cos(phi_r)) + zObj - a

yaw = theta - 180
pitch = -phi

print "gantry x = {0} y = {1} z = {2}, yaw joint {3} pitch joint {4}".format(x, y, z, yaw, pitch)

