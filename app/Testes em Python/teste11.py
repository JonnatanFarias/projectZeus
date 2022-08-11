import pyautogui
import math
import sys


SIZE_X, SIZE_Y = pyautogui.size()
# Uncoment to adjust screen size manualy
#SIZE_X = 1920
#SIZE_Y = 1080

STEPS = 90
TIME_STEP = 0.001

# Check if first arg is -h or -help and print usage message if so
if len(sys.argv) >=2:
	arg1 = sys.argv[1]

	if arg1 == "-h" or arg1 == "-help":
		print("\nMoves the mouse in a circle around the center of the screen.")
		print("\n\tUsage: circle.py [circle vertexe count] [tick length (seconds)]")
		exit(0)

# if vetex count is supplied, set the number of steps equal to vertex count
if len(sys.argv) >= 2:
	STEPS = int(sys.argv[1])
# if vertex count is supplied and tick length supplied, set the time for each
# mouse movement to tick length
if len(sys.argv) >= 3:
	TIME_STEP = float(sys.argv[2])

# generate 360 decimal coordiantes for a circle'ish shape mouse movement 
for i in range(0,STEPS):
	# Get the decimal coordinate of each 'tick' [0.0,1.0]
	# using sin/cos function
	j = (((i/STEPS)*2)*math.pi)
	x = math.cos(j) 
	y = math.sin(j) 
	# plot the mouse coordinates along a oval shape that
	# is centered on the middle of the screen.
	pyautogui.moveTo( SIZE_X/2 + (SIZE_Y/3)*x
			,SIZE_Y/2 + (SIZE_Y/3)*y, duration=TIME_STEP)