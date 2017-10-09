from graphics import *
import time

def main():
	win = GraphWin('The Return of the Elemelon', 400, 400)
	win.yUp()
	
	
	for i in range(48):
		watermelon.move(5,0)
		time.sleep(.05)
	
	for i in range(48):
		watermelon.move(-5,0)
		time.sleep(.05)
		
win.promptClose(win.getWidth()/2, 20)
