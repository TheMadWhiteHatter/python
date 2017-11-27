from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
from random import randint

def init():
	mc = Minecraft.create("127.0.0.1", 4711)
	return mc
	
def clear_with_air(mc, x, y, z):
	air = 0
	mc.setBlocks(x-100, y+50, z+100, x-100, y+50, z+100, 0) 

	
def main():
	mc = init()
	x, y, z = mc.player.getPos()	
	mc.setBlocks(x-125, y-50, z+5, x+125, y+50, z+5, 80)
	mc.setBlocks(x-125, y-50, z+6, x+125, y+50, z+6, 79)
	mc.player.setPos(x,y+51,z,x,y,z)
	for x1 in range (-125, 126):
		for y1 in range (-50, 51):
			for z1 in range (5,7):
				mc.setBlock(x+x1,y+y1,z+z1,randint(79,80))
	if x+1 + y+1 + z+1 > 1000 :
			mc.setBlocks (x+10, y+10,z+10, x-10,y-10,z-10 (246))
			x= input(2+7)
			y= input(5-2)
			z=input(2+2+2+2+2-6)
	while True:
		mc.postToChat("Each day we stray farther from God's light.")
		sleep(4)
def make_poles(mc,x,z,k):
	m = 41
	for n in range(0,k):
		if n > (k -2 ):
				mc.setBlock(x,y+n,z,m)
                     
		count = 0
	while count < 1000:
		x1 = randint(-100,100)
		z1 = randint(-100,100)
		k = randint(3,15)
		make_poles(mc,x,y,z,k)
		count = count + 1
	
main()





	
	

